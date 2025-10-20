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

# lightweight stubs for nav links so url_for resolves (replace with real pages later)
@app.route("/profile")
def profile():
    return redirect(url_for("index"))

@app.route("/contact")
def contact():
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)