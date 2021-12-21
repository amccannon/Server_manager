# here we will define the classes of database

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy

#define a class for the model
class User(db.Model):
    """User model"""

    #give the table a name

    __tablename__ = "members"

    id = db.Column(db.Integer, primary_key=True)  # ID
    firstname = db.Column(db.String(25), unique=True, nullable=False) #first name
    lastname = db.Column(db.String(25), unique=True, nullable=False) #lastname name
    email = db.Column(db.String(25), unique=True, nullable=False) #email
    password = db.Column(db.String(25), unique=True, nullable=False) #password
    team = db.Column(db.Integer, unique=True, nullable=False) #team

    db.create_all()
    


    #def __init__(self, firstname: str, lastname: str, email: str, password: str, team: int):
    #    self.firstname = firstname
    #   self.lastname = lastname
    #    self.email = email
    #    self.password = password
    #    self.team = team