from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.errorhandler(404)
def handle_404_error(e):
    return render_template("error-404.html")

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/about")
def aboutpage():
    return render_template("about.html")

app = app.run()