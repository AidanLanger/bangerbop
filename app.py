import os
import shelve
from flask import Flask, request, render_template
from persistence import Persistence

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"