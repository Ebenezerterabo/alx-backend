#!/usr/bin/env python3
""" 4-app """
from flask import Flask, render_template, g
from babel_flask import Babel
# Create an instance of Flask
app = Flask(__name__)
babel = Babel(app)


Config = __import__('0-app.py').Config

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app.config.from_object(Config)
# Create a single route
@app.route('/', methods=['GET'])
def index():
    """ return index page """
    return render_template('4-index.html')


# Create a localeselector from request
@babel.localeselector
def get_locale():
    """ get locale from request """
    # detect if the incoming request contains locale argument
    if request.args.get('locale') in app.config['LANGUAGES']:
        return request.args.get('locale=fr')
    
    user = getattr(g, 'user', None)
    if user and user.get('locale') in app.config['LANGUAGES']:
        return user.get('locale')

    return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_user():
    """ get user from request """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None

def get_timezone():
    """ get timezone from request """
    user = getattr(g, 'user', None)
    if user and user.get('timezone'):
        return user.get('timezone')
    return app.config['BABEL_DEFAULT_TIMEZONE']

@app.before_request
def before_request():
    """ before request """
    g.user = get_user()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
