#!/usr/bin/env python3
"""Route module for the API - Use user locale"""
from flask import Flask, request, render_template, g
from flask_babel import Babel
from os import getenv
from typing import Union

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Setup - Babel configuration"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)  # ← string yox, birbaşa class


def get_locale() -> str:
    """Determines best match for supported languages"""
    # 1. URL parameter
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # 2. User settings
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    # 3. Request header / default
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)  # ← yeni API


def get_user() -> Union[dict, None]:
    """Returns user dict if ID can be found"""
    login_as = request.args.get('login_as')
    if login_as:
        user_id = int(login_as)
        if user_id in users:
            return users.get(user_id)
    return None


@app.before_request
def before_request() -> None:
    """Finds user and sets as global on flask.g.user"""
    g.user = get_user()


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """GET /
    Return: 6-index.html
    """
    return render_template('6-index.html')


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
