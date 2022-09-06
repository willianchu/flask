from crypt import methods
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
  if not request.form.get("name") or request.form.get("sport") not in ["Kung-fu", "Karate", "Judo", "Capoeira"]:
    return render_template("failure.html")

  return render_template("success.html")