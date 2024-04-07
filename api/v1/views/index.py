#!/usr/bin/python3
"""
route for api_views blueprint
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.users import User
from models.pharmacy_store import PharmacyStore
from models.drugs import Drug
from models.user_searches import UserSearches
from models.user_favorites import UserFavorites
from models.user_drugs import UserDrug
from models.drug_store_inventory import DrugStoreInventory


@app_views.route('/status', methods=['GET'])
def status():
    """Returns a JSON status response."""
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False)
def stats():
    return jsonify({
        "users": storage.count(User),
        "pharmacies": storage.count(PharmacyStore),
        "favorites": storage.count(UserFavorites),
        "searches": storage.count(UserSearches),
        "inventory": storage.count(DrugStoreInventory),
        "drugs": storage.count(Drug)
    })
