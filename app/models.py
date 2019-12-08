from app import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # events -  evnts in which user takes part
    events = db.relationship('Event', backref='member', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password, )

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), index=True)
    date = db.Column(db.Date, index=True)

    def __repr__(self):
        return "{} : {}".format(self.name, self.date)

class User(db.Model):
    pass