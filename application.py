!#/usr.bin.python3
import os
import smtplib
from flask import Flask, render_template, request

# Configure app
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=["POST"])
def index():
    Book = request.form.get("Book")
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    date = request.form.get("date")
    comments = request.form.get("comments")
    if not Book or not name or not email or not phone or not date or not comments:
        return render_template("error.html", message="Please complete all fields")
    message = "Your request has been emailed to us!"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("lguecia@gmail.com", os.getenv("PASSWORD"))
    server.sendmail("lguecia@gmail.com", email, message)
    return render_template("bookingconfirmation.html")
