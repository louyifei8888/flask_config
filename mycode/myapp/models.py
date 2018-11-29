
from .ext import db

class Humen(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(40)
    )
    age = db.Column(
        db.Integer
    )
    def __init__(self, name, age):
        self.name = name
        self.age = age
        db.session.add(self)
        db.session.commit()
