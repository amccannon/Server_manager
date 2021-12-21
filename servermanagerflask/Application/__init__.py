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

# - POSTGRES_USER= postgres
# - POSTGRES_PW= testing1
# - POSTGRES_URL= main-database.chkovmh0wpxg.us-east-2.rds.amazonaws.com
# - POSTGRES_DB= Login/Info

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





#t_host = "main-database.chkovmh0wpxg.us-east-2.rds.amazonaws.com"
#t_host = "postgresql+psycopg2://main-database.chkovmh0wpxg.us-east-2.rds.amazonaws.com:5432"
#t_port = "5432"
#t_dbname = "postgres"
#t_user = "postgres"
#t_pw = "testing1"
#db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
#db_cursor = db_conn.cursor()
