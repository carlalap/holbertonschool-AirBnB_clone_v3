#!/usr/bin/python3
""" Script that starts an API! """
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os


""" Flask start """
app = Flask(__name__)

""" Register the blueprint app_views
for Flask instance """
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """ Method to handle that calls storage.close() """
    storage.close()


if __name__ == "__main__":
    API_HOST = os.getenv('HBNB_API_HOST', '0.0.0.0')
    API_PORT = int(os.getenv('HBNB_API_PORT', '5000'))

    app.run(host=API_HOST, port=API_PORT, threaded=True)
