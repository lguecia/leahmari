import os
import smtplib
from flask import Flask, render_template, request

# Configure app
app = Flask(__name__)


@app.route("/")
def index():
    Book = request.form.get("Book")
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    if not Book or not name or not email or not phone:
        return render_template("index.html")
    message = "Your request has been emailed to us!"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("lguecia@gmail.com", os.getenv("PASSWORD"))
    server.sendmail("lguecia@gmail.com", email, message)
    return render_template("bookingconfirmation_org.html")