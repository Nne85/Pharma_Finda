#!/usr/bin/python3

from flask import Flask, render_template, jsonify
from models import storage
from models.pharmacy_store import PharmacyStore
from models.drugs import Drug
from models.drug_store_inventory import DrugStoreInventory

app = Flask(__name__)

@app.route("/pharmacystores", methods=["GET"])
def get_all_pharmacaystores():
    pharmacy_stores = storage.all(PharmacyStore).values()
    return jsonify([pharmacy_store.to_dict() for pharmacy_store in pharmacy_stores])

@app.route('/drugs_by_pharmacies', strict_slashes=False)
def display_drugs_by_pharmacies():
    pharmacy_stores = storage.all(PharmacyStore).values()
    pharmacy_stores = sorted(pharmacy_stores, key=lambda x: x.name)
    pharm = []

    for pharmacy_store in pharmacy_stores:
        pharm.append([pharmacy_store, sorted(pharmacy_store.drugs, key=lambda k: k.name)])

    drugs = storage.all(Drug).values()
    drugs = sorted(drugs, key=lambda k: k.name)

    drug_store_inventory = storage.all(DrugStoreInventory).values()
    drug_store_inventory = sorted(drug_store_inventory, key=lambda k: k.name)

    return render_template('dashboard.html',
                            pharmacy_stores=pharm,
                            drugs=drugs,
                            drug_store_inventory=drug_store_inventory)


@app.route('/index', strict_slashes=False)
def display_drugs():
    return render_template('dashboard.html')



@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
