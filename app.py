import os
from flask import Flask, redirect, redirect, url_for, render_template, request, flash, jsonify
from flask_limiter import Limiter

app = Flask(__name__)
limiter = Limiter(app)

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/profile")
def profile():
    user = "Dariush"
    return render_template("profile.html", user=user)

@app.route("/admins")
@limiter.limit("5 per 30 seconds")
def admins():
    adminsList = ["Dariush", "Reyhane", "Shaghayegh"]
    return render_template("admins.html", adminsList=adminsList)

@app.route("/json")
@limiter.limit("5 per 10 seconds")
def jsonPage():
    data = {"message": "ok", "status": 200}
    return jsonify(data)

if __name__ == "__main__":
    app.run("0.0.0.0", 8001, debug=True)