"""Author: Oskar Malmquist, 2015"""

#importera flask
from flask import Flask, render_template

#skapa flask-appen
app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def startpage():
    return render_template("index.html")

if (__name__ == "__main__"):
    app.run()