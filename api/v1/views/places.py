#!/usr/bin/python3
"""Script for Place objects that handles
all default RESTFul API actions:"""
from api.v1.views import app_views
from models import storage
from models.city import City
from models.place import Place
from models.user import User
from flask import jsonify, abort, request


# Retrieves the list of all Place objects of a City:
# GET /api/v1/cities/<city_id>/places
@app_views.route("/cities/<city_id>/places", methods=["GET"],
                 strict_slashes=False)
def get_places_by_city(city_id):
    """Retrieves the list of all place objects by city"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    places = city.places
    return jsonify([place.to_dict() for place in places])


# Retrieves a Place object. : GET /api/v1/places/<place_id>
@app_views.route("/places/<place_id>", methods=["GET"], strict_slashes=False)
def get_place(place_id):
    """Retrieves a Place object."""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    return jsonify(place.to_dict())


# Deletes a Place object: DELETE /api/v1/places/<place_id>
@app_views.route("/places/<place_id>", methods=["DELETE"],
                 strict_slashes=False)
def delete_place(place_id):
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    storage.delete(place)
    storage.save()
    return jsonify({}), 200


# Creates a Place: POST /api/v1/cities/<city_id>/places
@app_views.route("/cities/<city_id>/places", methods=["POST"],
                 strict_slashes=False)
def create_place(city_id):
    """Create a new place object"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)

    place_data = request.get_json()
    if not place_data:
        abort(400, "Not a JSON")

    if "user_id" not in place_data.keys():
        abort(400, "Missing user_id")

    user = storage.get(User, place_data.get("user_id"))
    if not user:
        abort(404)

    if "name" not in place_data.keys():
        abort(400, "Missing name")

    place_data["city_id"] = city_id
    place = Place(**place_data)
    return jsonify(place.to_dict()), 201


# Updates a Place object: PUT /api/v1/places/<place_id>
@app_views.route("/places/<place_id>", methods=["PUT"], strict_slashes=False)
def update_place(place_id):
    """Updates an object"""
    place_data = request.get_json()
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    elif not place_data:
        abort(400, "Not a JSON")

    for key, value in place_data.items():
        if key not in ["id", "state_id", "city_id",
                       "created_at", "updated_at"]:
            setattr(place, key, value)
    storage.save()
    return jsonify(place.to_dict()), 200
