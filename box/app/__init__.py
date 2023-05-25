# import sqlite3  # for database building
import sqlite3

from flask import Flask # facilitate flask webserving
from flask import render_template  # facilitate jinja templating
from flask import request  # facilitate form submission
from flask import session  # facilitate user sessions

app=Flask(__name__) # create Flask object
# DO NOT EDIT ABOVE

@app.route("/")
def index():
        return render_template("index.html")

@app.route("/battering_ram")
def battering_ram():
        return render_template("battering_ram.html")

@app.route("/cluster_bomb")
def cluster_bomb():
        return render_template("cluster_bomb.html")

@app.route("/pitchfork")
def pitchfork():
        return render_template("pitchfork.html")

@app.route("/sniper")
def sniper():
        return render_template("sniper.html")


# DO NOT EDIT BELOW
if __name__ == "__main__":
app.run()