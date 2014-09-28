from app import app, mc1, mc2
from pymarkovchain import MarkovChain
from flask import render_template

@app.route("/")
def index():
    text =  mc1.generateString()
    comments = [mc2.generateString() for i in range(25)]
    return render_template("index.html", text = text, comments=comments)
