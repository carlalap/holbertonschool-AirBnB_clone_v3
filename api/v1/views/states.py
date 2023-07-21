#!/usr/bin/python3
"""Script for State objects that handles
all default RESTFul API actions:"""
from api.v1.views import app_views
from models import storage
from models.state import State
from flask import jsonify, request, abort


# Retrieves the list of all State objects - GET /api/v1/states
@app_views.route("/states", methods=["GET"], strict_slashes=False)
def retrieves_allstate():
    """Retrieves the list of all State objects"""
    states = storage.all(State).values()
    states_list = []
    for state in states:
        states_list. append(state.to_dict())
    return jsonify(states_list)


#  Retrieves a State object: GET /api/v1/states/<state_id>
@app_views.route("/states/<state_id>", methods=["GET"], strict_slashes=False)
def get_state(state_id):
    """Returns an State object by <state_id>"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())


# Deletes a State object:: DELETE /api/v1/states/<state_id>
@app_views.route("/states/<state_id>", methods=["DELETE"],
                 strict_slashes=False)
def delete_state(state_id):
    """Deletes a State object by <state_id>,
    if no state raise a 404 error, returns
    an empty dictionary with the status code 200"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


# Creates a State using POST /api/v1/states
@app_views.route("/states", methods=["POST"], strict_slashes=False)
def create_state():
    """Creates a State using Flask to transform
    the HTTP body request to a dictionary"""
    # retrieves state data and save in variable "state_request"
    state_request = request.get_json()
    if not state_request:
        abort(400, "Not a JSON")
    elif "name" not in state_request:
        abort(400, "Missing name")
    new_state = State(**state_request)
    new_state.save()
    # Returns the new State with the status code 201
    return jsonify(new_state.to_dict()), 201


# Updates a State object: PUT /api/v1/states/<state_id>
@app_views.route("/states/<int:state_id>", methods=["PUT"],
                 strict_slashes=False)
def update_state(state_id):
    """Update a State object based on <state_id>"""
    # retrieves state data from dict and save in variable "state_request"
    state_request = request.get_json()
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    elif not state_request:
        abort(400, "Not a JSON")

    for key, value in state_request.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200
