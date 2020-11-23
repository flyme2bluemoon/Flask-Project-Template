from helpers import *
from flask import Flask, redirect, request, render_template, session
from flask_session import Session

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return "Hello"

if __name__ == "__main__":
    app.run(host='0.0.0.0')