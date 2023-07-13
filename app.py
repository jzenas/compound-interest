
from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/process", methods=['GET', 'POST'])
def calc():
    print("hi")
    income = request.form.get("income")
    raises = request.form.get("raise")
    gains = request.form.get("gains")
    retire_age = request.form.get("retire")
    invest_percent = request.form.get("invest")
    current_ammount = request.form.get("current")
    current_age = request.form.get("age")

    return Flask.redirect("/")
