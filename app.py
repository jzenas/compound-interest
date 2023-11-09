
from flask import Flask
from flask import render_template, request, url_for, redirect

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    context = {"earnings": 0}
    return render_template("home.html", context=context)


@app.route("/process", methods=['GET', 'POST'])
def calc():
    print("hi")
    print(request.form)
    print("raise:" + request.form["raise"])
    income = float(request.form["income"])
    print("1")
    raises = float(request.form["raise"])/100
    print("1")
    gains = float(request.form["gains"]) / 100
    print("1")
    retire_age = int(request.form["retire"])
    print("1")
    invest_percent = float(request.form["invest"]) / 100
    print("1")
    current_ammount = int(request.form["current"])
    print("1")
    current_age = float(request.form["age"])

    time_diff = int(retire_age - current_age)

    value = current_ammount
    for i in range(0, time_diff):
        value = value * (1 + gains)
        value = value + (income * invest_percent)
        income = income*(1 + raises)
    context = {"earnings": int(value)}
    return render_template("home.html", context=context)

@app.route("/Contact/", methods=['GET', 'POST'])
def contact():
    return render_template("contact.html")

@app.route("/About/", methods=['GET', 'POST'])
def about():
    return render_template("about.html")

@app.route("/Tools/", methods=['GET', 'POST'])
def tools():
    return render_template("tools.html")