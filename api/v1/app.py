#!/usr/bin/python3
""" Script that starts an API! """
from flask import Flask, jsonify
from os import
from models import storage
from api.v1.views import app_views


""" Flask start """
app = Flask(__name__)

""" Register the blueprint app_views
for Flask instance """
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_app(exception):
    """ Method to handle that calls storage.close() """
    storage.close()


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True)
