#!/usr/bin/python3
"""
main Flask app
"""
import os
from os import getenv
from flask import Flask, Blueprint, jsonify
from models import storage
from models.users import User
from api.v1.views import app_views
from flask_cors import CORS
from models.custom_encoder import CustomJSONEncoder


app = Flask(__name__)
app.json_encoder = CustomJSONEncoder

app.register_blueprint(app_views, url_prefix='/api/v1')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

session_key = getenv('PHARMACY_SESSION_KEY')

app.secret_key = session_key



@app.teardown_appcontext
def close_storage(exception):
    """Closes the storage on teardown."""
    PHARMACY_ENV = getenv('PHARMACY_ENV')
    if PHARMACY_ENV == "db":
        storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """Handles 404 errors and returns a JSON response."""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.getenv('PHARMACY_API_HOST', '0.0.0.0')
    port = int(os.getenv('PHARMACY_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
