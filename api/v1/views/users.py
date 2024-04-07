#!/usr/bin/python3
"""
api view for users
"""
from api.v1.views import app_views
from flask import Flask, jsonify, request, abort, render_template, session, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import hashlib
from sqlalchemy import func
from sqlalchemy.orm import Session
from models import storage
from models.users import User
from models.pharmacy_store import PharmacyStore
from models.user_searches import UserSearches
from models.drug_store_inventory import DrugStoreInventory
from models.drugs import Drug
import os


from functools import wraps


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('appviews.login_user'))
        return f(*args, **kwargs)
    return decorated_function

def hash_password(password):
    return generate_password_hash(password)


@app_views.route("/users", methods=["GET"], strict_slashes=False)
def get_users():
    """Retrieves the list of all User objects."""
    users = storage.all(User).values()
    return jsonify([user.to_dict() for user in users])


@app_views.route("/users/<user_id>", methods=["GET"], strict_slashes=False)
def get_user(user_id):
    """Retrieves a User object by ID."""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route("/users/<user_id>", methods=["DELETE"], strict_slashes=False)
def delete_user(user_id):
    """Deletes a User object by ID."""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    user.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route("/register", methods=["GET", "POST"], strict_slashes=False)
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        location = request.form.get('location')

        existing_user = storage.get(User, email=email)
        if existing_user:
            flash("Email already registered.", "danger")
            return redirect(url_for("appviews.register"))

        new_user = User(name=name, email=email, password=password, location=location)
        new_user.save()
        flash("Registration successful.", "success")
        return redirect(url_for("appviews.landing_page"))

    return render_template("register.html")


@app_views.route("/users/<user_id>", methods=["PUT"], strict_slashes=False)
def update_user(user_id):
    """Updates a User object by ID."""
    updated = False
    updates = request.get_json()
    user = storage.get(User, user_id)
    if user:
        for key, value in updates.items():
            if key == 'id' or key == 'email' or key == 'created_at' or key == 'updated_at' or key == 'name':
                pass
            else:
                if key == 'password':
                    user.password = hash_password(value)['password']
                    updated = True
                elif key == 'name':
                    updated = True
                    user.name = value
        if updated:
            storage.new(user)
            storage.save()
        return jsonify(user.to_dict()), 200
    else:
        abort(400, description="Not a JSON")

@app_views.route("/login", strict_slashes=False, methods=['POST', 'GET'])
def login_user():
    """ check passed password and username against password and username stored in database """
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = storage.get(User, email=email)
        if user and user.password == hashlib.md5(password.encode()).hexdigest():
            session['user_id'] = user.id
            session['user_email'] = user.email
            print("Success")
            return redirect(url_for("appviews.landing_page"))
        else:
            print("Error")
            flash("Invalid email or password.", "danger")
            return redirect(url_for("appviews.login_user"))
    return render_template("login.html")


@app_views.route('/logout', methods=["GET"], strict_slashes=False)
@login_required
def logout():
    """
    logout from current session
    """
    session.clear()
    return redirect(url_for('appviews.logout_page'))


@app_views.route('/logout_page', methods=['GET'])
def logout_page():
    return render_template('logout.html')


@app_views.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
  user = storage.get(User, session['user_id'])
  # Retrieve saved searches or other user-specific information (implement logic using models)
  saved_searches = user.searches  # Assuming a relationship between User and UserSearches
  return render_template("dashboard.html", user=user, saved_searches=saved_searches)


@app_views.route("/", methods=["GET", "POST"])
def landing_page():
  if request.method == "POST":
    # Handle search query
    query = request.form.get("query")
    return redirect(url_for('appviews.search_results', query=query))
  else:
    return render_template("landing.html")


@app_views.route("/search", methods=["GET", "POST"])
def search_results():
    if request.method == "POST":
        # Handle search query from landing page form submission
        query = request.form.get("query")
        if query:
            return redirect(url_for('appviews.search_results', query=query))
        else:
            return redirect(url_for("appviews.landing_page"))
    else:
        # Process GET request (display search results)
        query = request.args.get("query")
        if not query:
            return redirect(url_for("appviews.landing_page"))

        # Create an instance of the storage
        storage.reload()

        # Query the database for drugs with a name similar to the query
        drugs = storage.all(Drug).values()
        pharmacy_stores = storage.all(PharmacyStore).values()
        filtered_drugs = [drug for drug in drugs if drug.name.lower() == query.lower()]

        # Prepare pharmacy and drug information
        pharmacies_with_info = []
        for drug in filtered_drugs:
            for store in pharmacy_stores:  # Access the pharmacy stores associated with the drug
                pharmacy_info = {
                    "name": store.name,
                    "address": store.address,
                    "city": store.city,
                    "state": store.state,
                    "drug_name": drug.name,
                    "price": drug.price,
                }
                pharmacies_with_info.append(pharmacy_info)

        # Remove duplicates based on pharmacy name (consider using a set)
        unique_pharmacies = []
        seen_pharmacies = set()
        for info in pharmacies_with_info:
            if info["name"] not in seen_pharmacies:
                unique_pharmacies.append(info)
                seen_pharmacies.add(info["name"])

        return render_template(
            "search_results.html",
            query=query,
            pharmacies=unique_pharmacies,
        )

def saved_searches(self, limit=5):
    """Returns the most recent searches for the user (up to limit)"""
    recent = UserSearches.query.filter_by(user_id=self.id).order_by(UserSearches.search_date.desc()).limit(limit)
    return recent.all()