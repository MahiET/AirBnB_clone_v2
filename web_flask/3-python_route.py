#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Start a basic Flask web application"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Adding a specific route /hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Dynamic inputed text: replace _ for space and show text"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is_cool"):
    """Dynamic inputed text: replace _ for space and show text"""
     text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
