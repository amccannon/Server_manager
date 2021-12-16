#routing 

from Application import app
from flask import render_template



#routes from now 

@app.route("/")
@app.route("/index")

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
    return render_template("servers.html")

#teams
@app.route("/teams")
def teams():
    return render_template("teams.html")

#terminal
@app.route("/terminal")
def terminal():
    return render_template("terminal.html")

#log out
@app.route("/alerts")
def alerts():
    return render_template("alerts.html")

#chat
@app.route("/chat")
def chat():
    return render_template("chat.html")

#Documentation
@app.route("/documentation")
def documentation():
    return render_template("documentation.html")


