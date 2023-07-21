#!/usr/bin/python3
"""Script that returns information"""

from api.v1.views import app_views
from flask import jsonify
from models import storage, classes


# created for Task_4. Status of your API
# create a route /status on the object app_views
# that returns a JSON: "status": "OK"
# curl -X GET http://0.0.0.0:5000/api/v1/status
@app_views.route('/status', methods=['GET'])
def get_status():
    """Endpoint to return the status as JSON
    status_data = {"status": "OK"}"""
    return jsonify(status_data)


# create for task 5
# @app_views.route('/api/v1/stats', methods=['GET'])
# def get_stats():
#    """Retrieve the number of each objects by type"""
#    stats = {}
#    for cls_name, cls in classes.items():
#        count = storage.count(cls)
#        stats[cls_name] = count
#
#    return jsonify(stats)
