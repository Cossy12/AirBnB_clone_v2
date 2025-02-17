#!/usr/bin/python3
"""
Flask  app
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
     hello hbnb
    """
    return 'Hello, HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
prints 
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """
     replaces _ with " " when printing c is fun
    """
    return "C " + text.replace("_", " ")


if (__name__) == "__main__":
    """
    Main function
    """
    app.run(host='0.0.0.0', port=5000)
