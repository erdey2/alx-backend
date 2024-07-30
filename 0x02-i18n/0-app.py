#!/usr/bin/env python3
""" Initial flask app """

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def welcome():
    """ display welcome """
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
