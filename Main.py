"""
This "Main.py" was tried to be kept clean by making sure only 'routes' are mentioned
and all the messy functions are kept in a different file.
"""

from flask import Flask, redirect, url_for, render_template , request


import ChatStuff as C
import ChatStuff_ForCustom as F
import txtHandler as T
from Modules import *

app = Flask(__name__)

"""I am not sure if setting every function under the routes as 'func' is a good practice.
It seems fine to me because they are only being called when a route is triggered and not explicitly for certain task to be accomplished

Please put up an issue for this if it is not considered a good practice, I shall correct this as soon as possible
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cust")
def func():
    return render_template("CustomEntries.html")

@app.route("/admin")
def func():
    return render_template("adminLogin.html")

@app.route("/help")
def func():
    return render_template("help.html")

@app.route("/work", methods=["GET", "POST"])
def func():
    user()

@app.route("/entries", methods=["GET", "POST"])
def func():
    custom()

@app.route("/login", methods=["GET", "POST"])
def func():
    logginchecker()

@app.route("/editsave", methods =["GET", "POST"])
def func():
    editer()

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')