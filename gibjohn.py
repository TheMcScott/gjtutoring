from flask import Flask, render_template, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Make the current year available to all templates
@app.context_processor
def inject_current_year():
    return {"current_year": datetime.utcnow().year}

@app.errorhandler(404)
def handle_404_error(e):
    return render_template("error-404.html"), 404

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/log-in")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)