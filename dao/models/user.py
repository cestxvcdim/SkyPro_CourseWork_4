from setup_db import db
from marshmallow import Schema, fields


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    favourite_genre = db.Column(db.String(255))
    role = db.Column(db.String(255))


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favourite_genre = fields.Str()
    role = fields.Str()
