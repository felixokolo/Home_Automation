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
    """
    Function to get user associated details or create a user

    Args:
        uname : String
            Username to fetch details
    """


    if request.method == 'GET':
        # Fetch user details
        locs = User.get_locs(uname)
        if locs is None:
            return jsonify(None)
        nodes = []
        for loc in locs:
            loc_node = Location.get_nodes(loc.id)
            if loc_node is not None:
                nodes += loc_node
        channels = []
        for node in nodes:
            channels.append({node.name: [ch.to_dict() for ch in node.get_channels()]})
        if channels is not None:
            return jsonify([channel for channel in channels])
        return jsonify(None)

    if request.method == 'POST':
        # Create a new user
        json_data = request.get_json(silent=True)
        if json_data is None:
            print("No Json")
            abort(404)
        try:
            new_user = User(**json_data)
        except Exception as e:
            print(e)
            return jsonify("'status': 'ERROR', 'reason': '{}'".format(e))
        try:
            new_user.save()
        except Exception as e:
            print(e)
            return jsonify("'status': 'ERROR', 'reason': '{}'".format(e))


        return jsonify("'status': 'OK', 'reason': 'Successful'")
