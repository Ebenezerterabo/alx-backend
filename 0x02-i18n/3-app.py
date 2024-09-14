#!/usr/bin/env python3
""" 3-app """
from flask import Flask, render_template
from babel_flask import Babel

Config = __import__('0-app.py').Config

# Create an instance of Flask and Babel
app = Flask(__name__)
babel = Babel(app)

app.config.from_object(Config)
# Create a single route
@app.route('/', methods=['GET'])
def index():
    """ return index page """
    return render_template('3-index.html')


# Create a localeselector from request
@babel.localeselector
def get_locale():
    """ get locale from request """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
