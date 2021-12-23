# Flask Application Testing
# 12/14/2021
# Antonino Abeshi

# now we have access to the flask application

from Application import models
from flask import Flask
# I will be using sha 256 encryption
from passlib.hash import pbkdf2_sha256 
import psycopg2 #database connection
from wtforms import *
from flask_login import login_manager, login_user, current_user
from flask_socketio import SocketIO, send, emit



# current application or module being rendered
app = Flask(__name__)
app.secret_key = 'replace later'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Instantiate Flask-SocketIO
socketio = SocketIO(app)


# Configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:testing1@main-database.chkovmh0wpxg.us-east-2.rds.amazonaws.com:5432/Login_info'
app.debug = True

# importing routes from Application
from Application import routes


#database 
models.db.init_app(app)


#Configuring the flask login

login = login_manager.LoginManager(app)
login.init_app(app)


#Using user loader to tell the login what a user is:
@login.user_loader
def load_user(id):

    return models.User.query.get(int(id))


#--------------------------------------------Creating Event Buckets or Handlers ---------------------------------------------------------


@socketio.on('message')  # predefined event
# we write a message to say what actions we want to take
def message(data):
    
    #for now
    print(f"\n\n{data}\n\n")


    #broadcast the message to the connected clients, on event bucket clients
    send(data)
    

    #braodcasting a message to some custom event
    #emit('some-event', 'this is a custom event message')




#t_host = "main-database.chkovmh0wpxg.us-east-2.rds.amazonaws.com"
#t_host = "postgresql+psycopg2://main-database.chkovmh0wpxg.us-east-2.rds.amazonaws.com:5432"
#t_port = "5432"
#t_dbname = "postgres"
#t_user = "postgres"
#t_pw = "testing1"
#db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
#db_cursor = db_conn.cursor()

if __name__ == "__main__":
    socketio.run(app, debug=True)