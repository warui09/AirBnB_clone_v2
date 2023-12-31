#!/usr/bin/python3
"""Starts a Flask web application
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the text variable
    /python/<text>: display “Python ”, followed by the value of the text
                    variable
"""

from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Display 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """Display 'C' followed by value of text with underscores replaced
    spaces"""
    try:
        if not text:
            abort(404)
        text = text.replace("_", " ")
        return f"C {text}"
    except Exception as e:
        abort(404)


@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text):
    """Display 'Python' followed by value of text with underscores replaced
    spaces"""
    try:
        if not text:
            text = "is cool"
        text = text.replace("_", " ")
        return f"Python {text}"
    except Exception as e:
        abort(404)


@app.errorhandler(404)
def page_not_found(e):
    """Handle the 404 error"""
    return render_template("404.html"), 404


if __name__ == "__main__":
    """Start the development server and listen on any address on port 5000"""
    app.run(host="0.0.0.0", port=5000)
