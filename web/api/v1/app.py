#!/usr/bin/python3
"""Web server app"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello_name(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
