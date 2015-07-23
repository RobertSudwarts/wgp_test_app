
from flask.ext.testing import TestCase
from nose.tools import *

from project import app, db
from project.models import Artist


class TestRoutes(TestCase):

    def create_app(self):
        app.config.from_object('config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Artist(age=42))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # tests that the main page is rendered
    def test_index(self):
        resp = self.client.get("/")
        self.assertIn('Filter by age range', resp.data)

    # tests that the callback returns a hash with the required variables
    def test_get_people(self):
        resp = self.client.get('/artists/38/45')
        assert_in('data', resp.json)
        assert_in('n', resp.json)
        assert_in('median', resp.json)
