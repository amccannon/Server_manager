#routing 

from Application import app
from Application import models
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

from Application.wtfform_fields import LoginForm, RegisterNewUser



#routes from now 

@app.route("/", methods=['GET','POST'])
@app.route("/index")

#---------------------------Login and Registering(new users----------------------------------------------------
#login
@app.route("/login")
def login():

    

    login_form = LoginForm()

    #allow login if works

    if login_form.validate_on_submit():
        return "Logged in"


    return render_template("login_test.html", form=login_form)
#registration
@app.route("/register", methods=['GET','POST'])

def register_test():

    reg_form = RegisterNewUser()

    # validatin, and return true, if false it will give us
    if reg_form.validate_on_submit():
        firstname = reg_form.firstname.data
        lastname = reg_form.lastname.data
        password = reg_form.password.data

        # Checking if the usernames exist

        user_object = models.User.query.filter_by(firstname=firstname).first()
        if user_object:
            return "It is already in the database!"


        #Adding user to database
        user = models.User(firstname=firstname, password=password)
        models.db.session.add(user)
        models.db.session.commit()

        return "Inserted into the DB"



    return render_template("register_test.html", form=reg_form)


#succesfull created a user
@app.route("/success_user")
def success_user():
    return render_template("success_user.html")

#-----------------------------------------------------------------------------------------------------

#main page
@app.route("/home")
def index():
    return render_template("index.html", login=False)

# settings
@app.route("/settings")
def settings():
    return render_template("/settings.html")

#activity_log
@app.route("/activity_log")
def activity_log():
    return render_template("activity_log.html")

#log out
@app.route("/logout")
def logout():
    return render_template("logout.html")

#-------------------------SideNav---------------------------------

#servers
@app.route("/servers")
def servers():

    serverData = [{"serverID":"someServerName","nameID":"Mathew","teamID":"The Bucaneers","healthID":"1234"},
    {"serverID":"someServerName","nameID":"Andrew","teamID":"Flags","healthID":"1235"},
    {"serverID":"someServerName","nameID":"Andrew","teamID":"Flags","healthID":"1236"},
    {"serverID":"someServerName","nameID":"Andrew","teamID":"Flags","healthID":"1237"}]
    
    #print(serverData)
    return render_template("servers.html", serverData=serverData)

#teams
@app.route("/teams")
def teams():

    teamsData = [{"teamnameID":"someServerName","teamadminID":"Mathew","numberofmembersID":"4","serverID":"1234"}]
    
    #print(teamsData)
    return render_template("teams.html", teamsData=teamsData)

#terminal
@app.route("/Jobs")
def terminal():

    jobsData = [{"teamnameID":"someServerName","jobsID":"This job"}]
    return render_template("jobs.html", jobsData=jobsData)

#log out
@app.route("/alerts")
def alerts():

    alertsData = [{"serverID":"someServerName","alertsID":"This server is in hight alert"}]

    return render_template("alerts.html", alertsData=alertsData)

#chat
@app.route("/chat")
def chat():
    return render_template("chat.html")

#Documentation
@app.route("/documentation")
def documentation():
    return render_template("documentation.html")


