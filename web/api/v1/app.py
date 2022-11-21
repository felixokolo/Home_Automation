#!/usr/bin/python3
"""Web server app"""
from flask import Flask
from markupsafe import escape
from web.models import storage
from web.models.user import User
from flask.json import jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello_name(name):
    return f"Hello, {name}!"

@app.route("/agile/<uname>")
def get_user_nodes(uname):
    nodes = User.get_user_nodes(uname)
    if nodes is not None:
        return jsonify([node.to_dict() for node in nodes])
    return jsonify(None)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
