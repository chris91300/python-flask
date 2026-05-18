# importe le module Flask
from flask import Flask, render_template, request

# créatio de l'instance du server web
app = Flask(__name__)


# HOME PAGE
@app.route("/", methods=["GET"])
def home():
    return render_template("homePage.html")


# FORM PAGE
@app.route("/form", methods=["GET"])
def form():
    return render_template("form.html")

# DASHBOARD PAGE
@app.route("/dashboard", methods=["POST"])
def dashboard():
    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    print(firstname)
    print(lastname)

    return render_template("dashboard.html", firstname=firstname, lastname=lastname)