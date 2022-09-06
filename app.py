from crypt import methods
from flask import Flask, render_template, request

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
  if not name:
    return render_template("error.html", message="Missing name")
  if sport not in SPORTS:
    return render_template("error.html", message="Invalid sport")
  
  # Remember registrant
  REGISTRANTS[name] = sport 

  # Confirm registration
  return redirect("/registrants")