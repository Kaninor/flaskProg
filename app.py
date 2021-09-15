import os
from flask import Flask, redirect, url_for, render_template, request, flash

app = Flask(__name__)

@app.route('/')
def home():
    name = "Dariush"
    return render_template("home.html", name=name)

@app.route("/profile")
def profile():
    return render_template("profile.html")

if __name__ == "__main__":
    app.run("0.0.0.0", 8001, debug=True)