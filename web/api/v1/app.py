#!/usr/bin/python3
"""Web server app"""
from flask import Flask
from markupsafe import escape
from web.models import storage
from web.models.user import User
from web.models.location  import Location
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
    locs = User.get_locs(uname)
    if locs is None:
        return jsonify(None)
    nodes = []
    for loc in locs:
        loc_node = Location.get_nodes(loc.id)
        if loc_node is not None:
            nodes += loc_node
    if nodes is not None:
        return jsonify([node.to_dict() for node in nodes])
    return jsonify(None)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
