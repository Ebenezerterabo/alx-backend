#!/usr/bin/env python3
""" 1-app """
from flask import Flask, render_template
from flask_babel import Babel
# Create an instance of Flask and Babel
app = Flask(__name__)
babel = Babel(app)
# Configure availabel languages
app.config['LANGUAGES'] = ['en', 'fr']
# Set the default language and timezone
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


# Create a single route
@app.route('/')
def index():
    """ return index page """
    return render_template('1-index.html')
