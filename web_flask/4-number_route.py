#!/usr/bin/python3
""" module doc """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ def doc """
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ hbnb func """
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c_is(text):
    return f'C {text.replace("_", " ")}'


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """ python func """
    return f'Python {text.replace("_", " ")}'


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ number func """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
