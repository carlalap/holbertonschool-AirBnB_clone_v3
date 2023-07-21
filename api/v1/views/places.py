#!/usr/bin/python3
"""Script for Place objects that handles
all default RESTFul API actions:"""
from api.v1.views import app_views
from models import storage
from models.city import City
from models.place import Place
from models.user import User
from flask import jsonify, request, abort


# Retrieves the list of all Amenity objects - GET /api/v1/amenities
@app_views.route("/cities/<city_id>/places", methods=["GET"], strict_slashes=False)
def retrieves_allamenity():
    """Retrieves the list of all Amenity objects"""
    amenities = storage.all(Amenity).values()
    amenities_list = []
    for amenity in amenities:
        amenities_list. append(amenity.to_dict())
    return jsonify(amenities_list)



