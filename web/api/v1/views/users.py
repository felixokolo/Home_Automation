#!/usr/bin/python3
""" Blueprint for API """
from web.api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from markupsafe import escape
from web.models import storage
from web.models.user import User
from web.models.location  import Location

@app_views.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app_views.route("/<uname>", methods=['GET', 'POST'])
def get_user_nodes(uname):
    if request.method == 'GET':
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

    if request.method == 'POST':
