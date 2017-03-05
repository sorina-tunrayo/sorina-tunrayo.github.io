from flask import Flask
from flask import render_template
from flask import request
import requests
app = Flask("MyApp")

Jericho = ["Lady_Margaret_Hall", "Somerville", "St_Johns", "St_Annes",\
 "Green_Templeton", "St_Benets", "St_Antonys", "Keble", "St_Johns", "St_Hughs"]
Botley = ["Ruskin", "Worcester", "Kellogg", "Regents_Park", "St_Cross", "Wolfson"]
Broad_street = ["Balliol", "Trinity", "Wadham", "Mansfield", "Harris_Manchester",\
"Linacre", "St_Catz"]
Bod_colleges = ["Exeter", "Jesus", "Lincoln", "Brasenose", "Hertford", "New",\
"All_Souls"]
Cowley = ["Queens", "Teddy_Hall", "University", "Merton", "Magdalen", "St_Hildas"]
Cornmarket = ["Oriel", "Corpus_Christi", "Christ_Church", "Pembroke", "Nuffield", "St_Peters"]


@app.route("/")
def outofhalls():
    return render_template("indexbod.html")

@app.route("/jericho")
def jericho():
    return render_template("jericho.html")

@app.route("/botley")
def botley():
    return render_template("botley.html")

@app.route("/broad_street")
def broad_street():
    return render_template("broad_street.html")

@app.route("/bod")
def bod():
    return render_template("bod.html")

@app.route("/cowley")
def cowley():
    return render_template("cowley.html")

@app.route("/cornmarket")
def cornmarket():
    return render_template("cornmarket.html")


def send_simple_message(var):
    print "sending email to {0}".format(var)
    return requests.post(
        "https://api.mailgun.net/v3/sandbox62c1649bfb464d9781537ad48f67a7dd.mailgun.org/messages",
        auth=("api", "key-b6e18fc0572d4d9c98c99abe2b4d2850"),
        data={"from": "Excited User <mailgun@sandbox62c1649bfb464d9781537ad48f67a7dd.mailgun.org>",
              "to": var,
              "subject": "Hello",
              "text": "Thank you for your email! We have taken your response and will review it shortly! Check back to see if your idea makes it onto the website!"})

@app.route("/signup", methods=['POST'])
def sign_up():
    form_data = request.form
    print form_data['name']
    email_address = form_data['email']
    print email_address
    print form_data['fave_spot']
    send_simple_message(email_address)
    return "All Ok."


app.run(debug = True)
