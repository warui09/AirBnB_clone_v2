#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Render the text "Hello HBNB"""
    return "Hello HBNB!"

if __name__ == "__main__":
    """Start the development server and listen on any address on port 5000"""
    app.run(host='0.0.0.0', port=5000)
