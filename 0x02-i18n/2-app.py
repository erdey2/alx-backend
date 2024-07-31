#!/usr/bin/env python3
"""Basic Babel setup  """

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """configuration Class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)

@babel.localselector
def get_local() -> str:
    """ select language translation """
    return request.accept_languages.best_match(app.config['LNAGUAGES'])


@app.route("/")
def welcome() -> str:
    """ Route path """
    return render_template("2-index.html")


if __name__ == '__main__':
    app.run(debug=True)
