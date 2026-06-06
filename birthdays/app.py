import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        # Validate submission
        if not name or not month or not day:
            return redirect("/")

        try:
            month = int(month)
            day = int(day)
        except ValueError:
            return redirect("/")

        if month < 1 or month > 12 or day < 1 or day > 31:
            return redirect("/")

        # Insert into database
        db.execute(
            "INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)",
            name,
            month,
            day,
        )

        return redirect("/")

    else:
        # Query for all birthdays
        birthdays = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", birthdays=birthdays)
# I’ve studied programming since 2018, including a technical high school in informatics and a degree in Systems Analysis and Development. I’ve done many programming courses and watched CS50 in 2023/2024. My solutions now rely only on my own knowledge, without rewatching lectures.
