#!/usr/bin/python3
"""Script that returns information"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def get_status():
    """Route to return a JSON response with status OK"""
    return jsonify(status="OK")
