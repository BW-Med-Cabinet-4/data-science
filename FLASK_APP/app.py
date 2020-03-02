"""Minimal flask app"""

from flask import Flask, render_template

#Make the application
app = Flask(__name__)

#Make the route
@app.route("/")

#Now define a function
def hello():
    return "Hello World!"

#MAke a second route
@app.route("/home")

#Function that goes with home
def preds():
    return render_template('home.html')
