# from crypt import methods
from email import message
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

REGISTRANTS = {}

SPORTS = [
  "Kung-fu",
  "Karate",
  "Muaytay",
  "Capoeira",
  "Jiujitsu"
]

@app.route("/")
def index():
  return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():
  # Validate name
  name = request.form.get("name")
  if not name:
    return render_template("error.html", message="Missing name")
  
  sport = request.form.get("sport")
  if not sport:
    return render_template("error.html", message="Missing sport")
  if sport not in SPORTS:
    return render_template("error.html", message="Invalid sport")
  
  # Remember registrant
  REGISTRANTS[name] = sport 

  # Confirm registration
  return redirect("/registrants")

@app.route("/registrants")
def registrants():
  return render_template("registrants.html", registrants=REGISTRANTS)