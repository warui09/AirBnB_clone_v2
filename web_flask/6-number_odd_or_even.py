#!/usr/bin/python3
"""Starts a Flask web application
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the text variable
    /python/<text>: display “Python ”, followed by the value of the text
                    variable
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY
    /number_odd_or_even/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n is even|odd” inside the tag BODY
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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is cool"):
    """Display 'Python' followed by value of text with underscores replaced
    spaces"""
    try:
        text = text.replace("_", " ")
        return f"Python {text}"
    except Exception as e:
        abort(404)


@app.route("/number/<n>", strict_slashes=False)
def is_number(n):
    """Display “n is a number” if n is an integer"""
    try:
        n = int(n)
        return f"{n} is a number"
    except ValueError:
        abort(404)


@app.route("/number_template/<n>", strict_slashes=False)
def is_number_template(n):
    """Display “Number is: n”"""
    try:
        n = int(n)
        return render_template("5-number.html", n=n)
    except ValueError:
        abort(404)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def is_number_odd_or_even(n):
    """Display “Number: n is odd | even”"""
    try:
        n = int(n)
        return render_template("6-number_odd_or_even.html", n=n)
    except ValueError:
        abort(404)


@app.errorhandler(404)
def page_not_found(e):
    """Handle the 404 error"""
    return render_template("404.html"), 404


if __name__ == "__main__":
    """Start the development server and listen on any address on port 5000"""
    app.run(host="0.0.0.0", port=5000)
