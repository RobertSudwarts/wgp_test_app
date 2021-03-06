
import os
from flask import Flask, render_template, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from collections import Counter

# Setup application
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

# Define the database object which is imported by modules and controllers
db = SQLAlchemy(app)

# current file's directory
cwd = os.path.dirname(os.path.abspath(__file__))

# note the [correct!] position of this import
from project.models import Artist


def midpoint(min_age, max_age):
    """
    Compute and return the median
    """
    return min_age + ((max_age - min_age) / 2)


def median_sort(data, min_age, max_age):
    """
    An interesting refresher:
    https://wiki.python.org/moin/HowTo/Sorting
    """
    mid = midpoint(min_age, max_age)
    return sorted(data, key=lambda p: abs(p['age'] - mid))


def buckets(data):
    """From the final (constrained) data we want to return a hash of:
    {
        'labels': [ <ages> ],
        'datasets': [
            {
                // count per bucket
                data: [28, 48, 40, 19, 86, 27, 90]
            }
        ]
    }
    """
    ages = [rw['age'] for rw in data]

    # user collections.Counter -- the result will be unordered
    counter = Counter(ages)

    # applying sorted() to the counter generates a list of tuples
    sorted_buckets = sorted(counter.items())

    # and now we split `sorted_buckets` into the components
    # required for the chart
    labels = [i[0] for i in sorted_buckets]

    dataset = {
        'fillColor': "rgba(151,187,205,0.5)",
        'strokeColor': "rgba(151,187,205,0.8)",
        'highlightFill': "rgba(151,187,205,0.75)",
        'highlightStroke': "rgba(151,187,205,1)",
        'data': [i[1] for i in sorted_buckets]
    }

    return dict(labels=list(labels), datasets=[dataset])


@app.route('/')
def index():
    """
        render the home/index page

    notice the prequery here for the absolute max/min ages: these are passed
    to the template for use in the slider control
    """
    mx = db.session.query(func.max(Artist.age)).scalar()
    mn = db.session.query(func.min(Artist.age)).scalar()

    return render_template('index.html', mx=mx, mn=mn)


@app.route('/artists/<int:min_age>/<int:max_age>')
def get_artists(min_age, max_age):
    """
        json callback used by knockout model
    """
    # 1. query and filter to constrain data by min/max boundaries
    rst = db.session.query(Artist) \
            .filter(Artist.age >= min_age) \
            .filter(Artist.age <= max_age)

    # 2. create a list from the recordset
    # notice that the UUID must be stringified
    data = [dict(uuid=str(rw.id), age=rw.age) for rw in rst]

    # 3. sort the data
    data = median_sort(data, min_age, max_age)

    # median value is recomputed and returned for display
    median = midpoint(min_age, max_age)

    chart_data = buckets(data)

    # import pdb; pdb.set_trace()

    return jsonify(data=data, n=len(data), median=median, chrt=chart_data)


#  the following functions are deprecated in favour of database calls
#  (ie these were used when reading data directly from the .json file)

# def clip_age_constraint(data, min_age, max_age):
#     """
#     list comprehension to reduce the `data` such that records are
#     constrained by:  min_age <= row age <= max_age
#     """
#     return [rw for rw in data if min_age <= rw['age'] <= max_age]


# @app.route('/getpeople/<int:min_age>/<int:max_age>')
# def get_people(min_age, max_age):
#     """
#     This works directly with the artists.json file
#     """
#     import json

#     with open(os.path.join(cwd, "artists.json"), 'rb') as fh:
#         data = json.load(fh)

#     # 1. constrain data by min/max boundaries
#     data = clip_age_constraint(data, min_age, max_age)

#     # 2. sort the data --- still not entirely happy with this...
#     data = median_sort(data, min_age, max_age)

#     # median value is recomputed and returned for display
#     median = midpoint(min_age, max_age)

#     return jsonify(data=data, n=len(data), median=median)
