# routing

from flask.helpers import make_response
from flask_login.utils import login_user, logout_user
from werkzeug.wrappers import request, response
from Application import ROOMS, app
from Application import models
from flask import render_template, redirect, url_for, flash, jsonify, make_response
from flask_sqlalchemy import *
from passlib.hash import pbkdf2_sha256
import psycopg2
import psutil
import os
import json
import matplotlib.pyplot as plt
import io
import base64
from time import time
from random import random



from Application.wtfform_fields import LoginForm, RegisterNewUser
from flask_login import login_manager, login_user, current_user, login_required, logout_user


# Connecting using psycopg2 to the database

try: 
    conn = psycopg2.connect(database="Login_info", user="postgres",  
    password="testing1", host="main-database.chkovmh0wpxg.us-east-2.rds.amazonaws.com",)
    print("connected")
except:
    print ("I am unable to connect to the database")

cursor = conn.cursor()
postgreSQL_select_Query = "select * from members"

#----------------------------Routes-------------------------------------------------

# routes from now

@app.route("/", methods=['GET', 'POST'])
@app.route("/index")
# ---------------------------Login and Registering(new users)----------------------------------------------------
# login
@app.route("/login", methods=['GET', 'POST'])
def login():

    login_form = LoginForm()

# allow login if works
    if login_form.validate_on_submit():

        #we need to pass in the login user
        user_object = models.User.query.filter_by(email=login_form.email.data).first()
        login_user(user_object)

        #current user is a proxy(based on documentation checking for user authentication)
        if current_user.is_authenticated:
            return redirect(url_for("index"))
            #return "Logged in with Flask - user"

        return redirect(url_for("login"))
        #return "Not loged in"

    return render_template("login_test.html", form=login_form)

# -------------------------------------------Registering(new users) (only Admin)----------------------------------------------------
@app.route("/register", methods=['GET', 'POST'])
def register_test():

    reg_form = RegisterNewUser()

    # validatin and should add to the database
    if reg_form.validate_on_submit():
        firstname = reg_form.firstname.data
        lastname = reg_form.lastname.data
        email = reg_form.email.data
        password = reg_form.password.data
        teams = reg_form.teams.data


        #Applying SHA - 256 - encryption (automatically applies the salt (16 byte) and (29000 iterations))
        # to Modify it we would do pbkdf2_sha256.using(rounds=1000, salt_size=8).(password) - no reason though

        # Hashed password
        hashed_pswd = pbkdf2_sha256.hash(password)

        # Adding user to database
        user = models.User(firstname=firstname, lastname=lastname,
                           email=email, password=hashed_pswd, teams=teams)
        models.db.session.add(user)
        models.db.session.commit()

        #flashing the user before registering, category
        flash('Registered Successfully, the user can now log in.' , 'success')

        return redirect(url_for("success_user"))

    return render_template("register_test.html", form=reg_form)


# succesfull created a user
@app.route("/success_user")
def success_user():
    return render_template("success_user.html")

# -------------------------------------LogOut----------------------------------------------------------------

@app.route("/logout", methods=["GET"])
def logout():


    logout_user()
    flash('You are logged out.', 'success')


    #loged out using flask
    #return "Logged out usign flask login"
    return render_template("logout.html")


#-----------------------------------------------------------------------------------------------------------

# main page
@app.route("/home")
@login_required
def index():
    return render_template("index.html", login=False)

# settings


@app.route("/settings")
@login_required
def settings():
    return render_template("/settings.html")

# activity_log


@app.route("/activity_log")
@login_required
def activity_log():
    return render_template("activity_log.html")


# -------------------------SideNav---------------------------------

###########################Servers


@app.route("/servers")
@login_required
def servers():

    serverData = [{"serverID": "someServerName", "nameID": "Mathew", "teamID": "The Bucaneers", "healthID": "1234"}]

    # print(serverData)
    return render_template("servers.html", serverData=serverData)

@app.route("/graph")
@login_required
def graph():
    return render_template('graph.html')

@app.route('/data', methods=["GET", "POST"])
@login_required
def data():


    cpu = psutil.cpu_percent()
    v_memory = psutil.virtual_memory()
    ram = psutil.virtual_memory().percent 
    avail_ram = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total



    data = [time() * 1000, cpu, ram, v_memory, avail_ram]
    response = make_response(json.dumps(data))
    response.content_type = "application/json"
    return response
    
    #return render_template('graph.html')
    #return jsonify ({'results' : cpu_percent})




##############################Teams


@app.route("/teams", methods=['GET','POST'])
@login_required
def teams():

    cursor.execute(postgreSQL_select_Query)
    print("selecting rows from members using cursor.fetchall")
    members_all = cursor.fetchall()

    #print("Print each row and it's columns values")
    #for row in members_all:
        #print("Id = ", row[0], )
        #print("FirstName = ", row[1])
        #print("Lastname  = ", row[2], "\n")

    #-----Needs Work----#
    if request.method == 'POST':
        if request.form.get('Delete') == 'Delete':
            cursor.execute("DELETE FROM members WHERE id = %s", id)
        else:
            pass # unknown

    # print(teamsData)
    return render_template("teams.html", data = members_all)

#############################Terminal


@app.route("/Jobs")
@login_required
def terminal():

    jobsData = [{"teamnameID": "someServerName", "jobsID": "This job"}]
    return render_template("jobs.html", jobsData=jobsData)

# log out


@app.route("/alerts")
@login_required
def alerts():

    alertsData = [{"serverID": "someServerName",
                   "alertsID": "This server is in hight alert"}]

    return render_template("alerts.html", alertsData=alertsData)

#----------------------------------CHAT---------------------------------------------


@app.route("/chat", methods=['GET','POST'])
# checking if the user is authenticated or not (if user is using this feature withought login in there will be an error)
#@login_required
def chat():

    #if not current_user.is_authenticated:
    #    flash('Please login to use the chat', 'danger')
    #    return "Please log in before accessing the site"
    #return render_template("chat.html")
    return render_template("chat.html", firstname=current_user.firstname, rooms=ROOMS)

# Documentation


@app.route("/documentation")
@login_required
def documentation():
    return render_template("documentation.html")
