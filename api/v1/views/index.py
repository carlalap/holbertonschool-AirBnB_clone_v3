#!/usr/bin/python3
"""Script that returns information"""

from flask import jsonify
from api.v1.views import app_views
from models import storage


# created for Task_4. Status of your API
# create a route /status on the object app_views
# that returns a JSON: "status": "OK"
# curl -X GET http://0.0.0.0:5000/api/v1/status
@app_views.route('/status', methods=['GET'])
def status():
    """ Returns a JSON: "status": "OK """
    return jsonify(status="OK")


# create for task 5
@app_views.route('/api/v1/stats', methods=['GET'])
def get_stats():
    """Retrieve the number of each objects by type"""
    stats = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    }
    json_dict = json.dumps(dic, indent=2)
    return json_dict
    

