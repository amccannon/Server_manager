# Flask Application Testing
# 12/14/2021
# Antonino Abeshi

# now we have access to the flask application

import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import psycopg2 #database connection
from wtforms import *

# current application or module being rendered
app = Flask(__name__)
app.secret_key = 'replace later'

# this can be the root directory (decorators using these different types of urls)

# importing routes from Application
from Application import routes

# database connection
app.config['SQLALCHEMY_DATABASE_URI'] = "main-database.chkovmh0wpxg.us-east-2.rds.amazonaws.com"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#database and migrate
db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)


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
    


    def __init__(self, firstname: str, lastname: str, email: str, password: str, team: int):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.team = team




t_host = "main-database.chkovmh0wpxg.us-east-2.rds.amazonaws.com"
#t_host = "postgresql+psycopg2://main-database.chkovmh0wpxg.us-east-2.rds.amazonaws.com:5432"
t_port = "5432"
t_dbname = "postgres"
t_user = "postgres"
t_pw = "testing1"
db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
db_cursor = db_conn.cursor()
