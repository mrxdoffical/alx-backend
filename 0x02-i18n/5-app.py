#!/usr/bin/env python3
"""A Basic Flask app with Babel setup, locale selection, and user login mock.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _


class Config:
    """Configuration for Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> dict:
    """Retrieve a user dictionary or None if the ID is not found."""
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request() -> None:
    """Set the user in the global context before each request."""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Determine the best match for supported languages."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def get_index() -> str:
    """The home/index page."""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
