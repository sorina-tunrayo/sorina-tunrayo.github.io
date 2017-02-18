from flask import Flask
from flask import render_template
from flask import request
import requests
app = Flask("MyApp")

Jericho = ["Lady_Margaret_Hall", "Somerville", "St_Johns", "St_Annes"]
Botley = [""]
Broad_street = [""]
Bod_colleges = [""]
Cowley = ["Queens", "Teddy_Hall", "Univ"]
Cornmarket = [""]


@app.route("/")
def normal():
    return render_template("outofhalls.html")

@app.route("/<Jer")
def group_one(class1):
    return render_template("outofhalls.html", )
