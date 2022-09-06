from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
  # name = request.args.get("name")
  # , name=name)
  return render_template("index.html")   

@app.route("/greet")
def greet():
  name = request.args.get("name", "What ever!")
  return render_template("greet.html", name=name)