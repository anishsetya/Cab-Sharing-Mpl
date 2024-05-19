from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import date, timedelta

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    email= db.Column(db.String(150),unique=True)
    password=db.Column(db.String(150))
    name=db.Column(db.String(150))
    
class Request(db.Model):
    request_id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    flight_time = db.Column(db.Time)
    date = db.Column(db.Date)
    vacancy = db.Column(db.Integer)

class Matches(db.Model):
    matchid=db.Column(db.Integer, primary_key=True)
    userid1 = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    userid2 = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
