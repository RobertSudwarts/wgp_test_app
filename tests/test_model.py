
from flask.ext.testing import TestCase

from project import app, db
from project.models import Artist


class TestArtist(TestCase):
    """
      Test model session.add(Artist())
    """
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
