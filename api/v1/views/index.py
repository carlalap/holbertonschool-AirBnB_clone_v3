#!/usr/bin/python3
"""Script that returns information"""

from api.v1.views import app_views
from flask import jsonify
from models import storage, classes



@app_views.route('/status', methods=['GET'])
def get_status():
    """Route to return a JSON response with status OK"""
    return jsonify(status="OK")


@app_views.route('/api/v1/stats', methods=['GET'])
def get_stats():
    """Retrieve the number of each objects by type"""
    stats = {}
    for cls_name, cls in classes.items():
        count = storage.count(cls)
        stats[cls_name] = count

    return jsonify(stats)
