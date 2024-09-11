#!/usr/bin/env python3
""" 0-app """
from flask import Flask, render_template
# Create an instance of Flask
app = Flask(__name__)


# Create a single route
@app.route('/')
def index():
    return render_template('0-index.html')
