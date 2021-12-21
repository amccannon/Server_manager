# Flask Application Testing
# 12/14/2021
# Antonino Abeshi

# now we have access to the flask application

from Application import models
from flask import Flask
import psycopg2 #database connection
from wtforms import *



# current application or module being rendered
app = Flask(__name__)
app.secret_key = 'replace later'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:testing1@main-database.chkovmh0wpxg.us-east-2.rds.amazonaws.com:5432/Login_info'
app.debug = True

# importing routes from Application
from Application import routes

# database connection


#database 
models.db.init_app(app)




#t_host = "main-database.chkovmh0wpxg.us-east-2.rds.amazonaws.com"
#t_host = "postgresql+psycopg2://main-database.chkovmh0wpxg.us-east-2.rds.amazonaws.com:5432"
#t_port = "5432"
#t_dbname = "postgres"
#t_user = "postgres"
#t_pw = "testing1"
#db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
#db_cursor = db_conn.cursor()
