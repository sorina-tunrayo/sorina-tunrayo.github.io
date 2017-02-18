from flask import Flask
from flask import render_template
from flask import request
import requests
app = Flask("MyApp")

Jericho = ["Lady_Margaret_Hall", "Somerville", "St_Johns", "St_Annes",/
 "Green_Templeton", "St_Benets", "St_Antonys", "Keble", "St_Johns", "St_Hughs"]
Botley = ["Ruskin", "Worcester", "Kellogg", "Regents_Park", "St_Cross", "Wolfson"]
Broad_street = ["Balliol", "Trinity", "Wadham", "Mansfield", "Harris_Manchester",/
"Linacre", "St_Catz"]
Bod_colleges = ["Exeter", "Jesus", "Lincoln", "Brasenose", "Hertford", "New",/
"All_Souls"]
Cowley = ["Queens", "Teddy_Hall", "University", "Merton", "Magdalen", "St_Hildas"]
Cornmarket = ["Oriel", "Corpus_Christi", "Christ_Church", "Pembroke", "Nuffield", "St_Peters"]


@app.route("/")
def normal():
    return render_template("outofhalls.html")

@app.route("/<Jer")
def group_one(class1):
    return render_template("outofhalls.html", )
