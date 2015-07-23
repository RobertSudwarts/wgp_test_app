
import os
import json
from project import db
from project.models import *

# current file's directory
cwd = os.path.dirname(os.path.abspath(__file__))

db.create_all()


def bootstrap():
    """
    Bootstrap data from .json
    """
    with open(os.path.join(cwd, "project", "artists.json"), 'rb') as fh:
        data = json.load(fh)

    for row in data:
        artist = Artist(id=row['uuid'], age=row['age'])
        db.session.add(artist)


bootstrap()

# commit changes
db.session.commit()
