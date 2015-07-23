import uuid
from guid import GUID
from project import db


class Artist(db.Model):
    __tablename__ = "artists"
    id = db.Column(GUID(), default=uuid.uuid4, primary_key=True)
    age = db.Column(db.Integer)
