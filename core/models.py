from typing import Collection
from flask_login import UserMixin
from core import db
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    gender = db.Column(db.String(10),nullable=False)
    date_of_birth = db.Column(db.Date,nullable=False)
    password = db.Column(db.String(20), nullable=False)
    is_writer = db.Column(db.String(10),nullable=False)
    posts = db.relationship('Post',backref='author',lazy=True)

    def __repr__(self):
        return f'User {self.id}'


class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    date_created = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Post ({self.title},{self.date_created  })"
