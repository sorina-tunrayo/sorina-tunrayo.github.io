from flask import Flask
from flask import render_template
from flask import request

app = Flask("MyApp")

Jericho = ["Lady_Margaret_Hall", "Somerville", "St_Johns", "St_Annes",\
 "Green_Templeton", "St_Benets", "St_Antonys", "Keble", "St_Johns", "St_Hughs"]
Botley = ["Ruskin", "Worcester", "Kellogg", "Regents_Park", "St_Cross", "Wolfson"]
Broad_street = ["Balliol", "Trinity", "Wadham", "Mansfield", "Harris_Manchester",\
"Linacre", "St_Catz"]
Bod_colleges = ["Exeter", "Jesus", "Lincoln", "Brasenose", "Hertford", "New",\
"All_Souls"]
Cowley = ["Queens", "Teddy_Hall", "University", "Merton", "Magdalen", "St_Hildas"]
Cornmarket = ["Oriel", "Corpus_Christi", "Christ_Church", "Pembroke", "Nuffield",\
"Pembroke", "Nuffield", "St Peter's"]

@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
#        return render_template('post.html');
        return render_template('homepage_test.html');
        return render_template("jericho.html")
        return render_template("botley.html")
        return render_template("broad_street.html")
        return render_template("bod.html")
        return render_template("cowley.html")
        return render_template("cornmarket.html")
           
app.run(debug = True)
