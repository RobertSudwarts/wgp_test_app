wgp test
=================

.. image:: https://travis-ci.org/RobertSudwarts/wgp_test_app.svg?branch=master
    :target: https://travis-ci.org/RobertSudwarts/wgp_test_app


task
----------------

Implement a simple search service (complete with suitable test coverage) using
any Python web framework (micro frameworks welcome). The purpose is to find
artists that match an age range (minimum to maximum) where results are ordered
by best fit. The best fit algorithm is open to your choice, but should favour
artists with ages in the middle of the range over those at the edge of the
range.

The output from the search function should be a JSON encoded structure with a
list of matching artist UUIDs and ages. The dataset is in the attached
'artists.json' file.”


setup
-------

In a clean virtual environment:

    $ pip install -r requirements.txt

An additional dev_requirements.txt is available for installation of ipython
the ipython notebook and its dependencies


database
---------

The git repository contains a working sqlite file, `app.db` but this can be
deleted and recreated with:

    $ python create_db.py


running the application
-------------------------

To serve the application on port 8080:

    $ python run.py


tests
-------

There is 100% code coverage. And the git repository is tracked/covered by Travis CI.

