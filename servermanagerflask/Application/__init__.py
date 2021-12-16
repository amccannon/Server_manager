# Flask Application Testing
# 12/14/2021
# Antonino Abeshi

# now we have access to the flask application

from flask import Flask
import psycopg2 #database connection
from wtforms import *

# current application or module being rendered
app = Flask(__name__)
app.secret_key = 'replace later'

# this can be the root directory (decorators using these different types of urls)

# importing routes from Application
from Application import routes

#t_host = "main-database.chkovmh0wpxg.us-east-2.rds.amazonaws.com"
#t_port = "5432"
#t_dbname = "database name"
#t_user = "postgres"
#t_pw = "testing1"
#db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
#db_cursor = db_conn.cursor()