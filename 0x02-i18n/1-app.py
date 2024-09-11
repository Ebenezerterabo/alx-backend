#!/usr/bin/env python3
""" 1-app """
from flask import Flask, render_template
from flask_babel import Babel
# Create an instance of Flask and Babel
app = Flask(__name__)
babel = Babel(app)


# Create a Config Class
class Config():
    """ Config Class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Set the config with the Config Class
app.config.from_object(Config)


# Create a single route
@app.route('/')
def index():
    """ return index page """
    return render_template('1-index.html')
