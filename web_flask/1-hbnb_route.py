#!/usr/bin/python3
"""Starts a Flask web application
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Display 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display 'HBNB'"""
    return "HBNB"


if __name__ == "__main__":
    """Start the development server and listen on any address on port 5000"""
    app.run(host="0.0.0.0", port=5000)
