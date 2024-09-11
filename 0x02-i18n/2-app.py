#!/usr/bin/env python3
""" 2-app """
from flask import Flask, render_template, request
from flask_babel import Babel
# Create an instance of Flask and Babel
app = Flask(__name__)
babel = Babel(app)


# Create a localeselector from request
@babel.localeselector
def get_locale():
    """ get locale from request """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# Create a single route
@app.route('/')
def index():
    """ return index page """
    return render_template('2-index.html')
