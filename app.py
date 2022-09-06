from flask import Flask, render_template, request

app = flask (__name__)

@app.route("/")
def index():
  return render_template("index.html")