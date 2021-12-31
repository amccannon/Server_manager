# Flask Application Testing
# 12/14/2021
# Antonino Abeshi

# now we have access to the flask application
from os import name
from time import localtime,strftime
from Application import models
from flask import Flask
from flask import render_template, redirect, url_for, flash, jsonify, make_response
# I will be using sha 256 encryption
from passlib.hash import pbkdf2_sha256 
import psycopg2 #database connection
from wtforms import *
from flask_login import login_manager, login_user, current_user
from flask_socketio import SocketIO, send, emit, join_room, leave_room

#----------------------------------------------------------------------------------
# Check server

import socket
import ssl
from datetime import datetime

import subprocess
import platform

#--------------------------------------------------------------------------------------




# current application or module being rendered
app = Flask(__name__)
app.secret_key = 'replace later'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Instantiate Flask-SocketIO
socketio = SocketIO(app)
ROOMS = ["support", "team", "main"]

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

    room = data.get('room')
    #broadcast the message to the connected clients, on event bucket clients (issue with room=data('room'))
    send({'msg': data['msg'], 'firstname': data['firstname'], 'timestamp': strftime('%b-%d %I:%M %p', localtime())}, room=data['room'])
    #current_user.firstname  

#-----------------------------------Joining and Leaving a Room-----------------------------
# Joining a room
@socketio.on('join')
def join(data):

    #Getting a user to join a room
    join_room(data['room'])
    send({'msg': data['firstname'] + " has joined the " + data['room'] + " room."}, room=data['room'])

# Leaving a room

@socketio.on('leave')
def leave(data):

    #Getting a user to join a room
    leave_room(data['room'])
    send({'msg': data['firstname'] + " has left the " + data['room'] + " room."}, room=data['room'])


#------------------------------------------------------Check Server------------------------------------------------------------

class Server():
    def __init__(self, name, port, connection, priority):
        self.name = name
        self.port = port
        self.connection = connection.lower()
        self.priority = priority.lower()

        self.history = []
        self.alert = False

    def check_connection(self):
        msg = ""
        success = False
        now = datetime.now()

        try:
            if self.connection == "plain":
                socket.create_connection((self.name, self.port), timeout=10)
                msg = f"{self.name} is up. On port {self.port} with {self.connection}"
                success = True
                self.alert = False
            elif self.connection == "ssl":
                ssl.wrap_socket(socket.create_connection((self.name, self.port), timeout=10))
                msg = f"{self.name} is up. On port {self.port} with {self.connection}"
                success = True
                self.alert = False
            else:
                if self.ping():
                    msg = f"{self.name} is up. On port {self.port} with {self.connection}"
                    success = True
                    self.alert = False
        except socket.timeout:
            msg = f"server: {self.name} timeout. On port {self.port}"
        except (ConnectionRefusedError, ConnectionResetError) as e:
            msg = f"server: {self.name} {e}"
        except Exception as e:
            msg = f"No Clue??: {e}"

        self.create_history(msg,success,now)

    def create_history(self, msg, success, now):
        history_max = 100
        self.history.append((msg,success,now))

        while len(self.history) > history_max:
            self.history.pop(0)

    def ping(self):
        try:
            output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower(
            ) == "windows" else 'c', self.name ), shell=True, universal_newlines=True)
            if 'unreachable' in output:
                return False
            else:
                return True
        except Exception:
                return False


#t_host = "main-database.chkovmh0wpxg.us-east-2.rds.amazonaws.com"
#t_host = "postgresql+psycopg2://main-database.chkovmh0wpxg.us-east-2.rds.amazonaws.com:5432"
#t_port = "5432"
#t_dbname = "postgres"
#t_user = "postgres"
#t_pw = "testing1"
#db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
#db_cursor = db_conn.cursor()

@app.route("/alerts")
#@login_required
def alerts():

    servers = [
    Server("ec2-18-188-42-85.us-east-2.compute.amazonaws.com", 22, "plain", "high"),
        #Server("ec2-18-116-237-91.us-east-2.compute.amazonaws.com", 22, "plain", "high") 
    ]


    for server in servers:
        server.check_connection()
        print(len(server.history))
        print(server.history[-1])
    
        alertsData = [{"serverID": server.check_connection(), 
                    "connectionID": len(server.history),
                    "history": server.history[-1]
                        }]

    return render_template("alerts.html", alertsData=alertsData)

if __name__ == "__main__":
    socketio.run(app, debug=True)

    