#!/usr/bin/python3
"""Script for Amenity objects that handles
all default RESTFul API actions:"""
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from flask import jsonify, request, abort


# Retrieves the list of all Amenity objects - GET /api/v1/amenities
@app_views.route("/amenities", methods=["GET"], strict_slashes=False)
def retrieves_allamenity():
    """Retrieves the list of all Amenity objects"""
    amenities = storage.all(Amenity).values()
    amenities_list = []
    for amenity in amenities:
        amenities_list. append(amenity.to_dict())
    return jsonify(amenities_list)


#  Retrieves a Amenity object: GET /api/v1/amenities/<amenity_id>
@app_views.route("/amenities/<amenity_id>", methods=["GET"],
                 strict_slashes=False)
def get_amenity(amenity_id):
    """Returns an Amenity object by <amenity_id>"""
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    return jsonify(amenity.to_dict())


# Deletes a Amenity object:: DELETE /api/v1/amenities/<amenity_id>
@app_views.route("/amenities/<amenity_id>", methods=["DELETE"],
                 strict_slashes=False)
def delete_amenity(amenity_id):
    """Deletes a Amenity object by <amenity_id>,
    if no amenity raise a 404 error, returns
    an empty dictionary with the status code 200"""
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200


# Creates a Amenity using POST /api/v1/amenities
@app_views.route("/amenities", methods=["POST"], strict_slashes=False)
def create_amenity():
    """Creates a Amenity using Flask to transform
    the HTTP body request to a dictionary"""
    # retrieves amenity data and save in variable "amenity_request"
    amenity_request = request.get_json()
    if not amenity_request:
        abort(400, "Not a JSON")
    elif "name" not in amenity_request:
        abort(400, "Missing name")
    new_amenity = Amenity(**amenity_request)
    new_amenity.save()
    # Returns the new Amenity with the status code 201
    return jsonify(new_amenity.to_dict()), 201


# Updates a Amenity object: PUT /api/v1/amenities/<amenity_id>
@app_views.route("/amenities/<int:amenity_id>", methods=["PUT"],
                 strict_slashes=False)
def update_amenity(amenity_id):
    """Update a Amenity object based on <amenity_id>"""
    # retrieves amenity data from dict and save in variable "amenity_request"
    amenity_request = request.get_json()
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    elif not amenity_request:
        abort(400, "Not a JSON")

    for key, value in amenity_request.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, value)
    amenity.save()
    return jsonify(amenity.to_dict()), 200
