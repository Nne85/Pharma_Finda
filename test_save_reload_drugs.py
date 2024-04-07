#!/usr/bin/python3
from models import PHARMACY_Storage
from models.base_model import BaseModel
from models.drugs import Drug
from models.pharmacy_store import PharmacyStore

db = PHARMACY_Storage()
db.reload()
all_drugs = db.all(Drug)

print("-- Reloaded objects --")
for obj_id in all_drugs.keys():
    obj = all_drugs[obj_id]
    print(obj)

# Retrieve all PharmacyStore objects
all_stores = db.all(PharmacyStore)

print("-- Reloaded pharmacy stores --")
for obj_id in all_stores.keys():
    obj = all_stores[obj_id]
    print(obj)

print("-- Create a new Drug --")
my_drugs = Drug()
my_drugs.name = "Diclofenac"
my_drugs.price= 200.55
my_drugs.description = "Pain Reliever"
my_drugs.category = "Pain Management"
my_drugs.in_stock = bool(my_drugs)
my_drugs.save()
print(my_drugs)

print("-- Create a new Drug 2 --")
my_drugs = Drug()
my_drugs.name = "Paracetemol"
my_drugs.price= 200.55
my_drugs.description = "Pain Reliever"
my_drugs.category = "Pain Management"
my_drugs.in_stock = True
my_drugs.save()
print(my_drugs)

print("-- Create a new Drug 3 --")
my_drugs = Drug()
my_drugs.name = "Vitamin C"
my_drugs.price= 200.55
my_drugs.description = "Multivitamin"
my_drugs.category = "Supplement"
my_drugs.in_stock = True
my_drugs.save()
print(my_drugs)


print("-- Create a new PharmacyStore (if not already created) --")
# Check if a store already exists, otherwise create a new one
existing_store = db.all(PharmacyStore).get("store_id", None)
if not existing_store:
  my_pharmacy_store = PharmacyStore()
  my_pharmacy_store.name = "Abki Pharmacy"  # Replace with actual store details
  my_pharmacy_store.address = "55 Main Street"
  my_pharmacy_store.city = "Lagos"
  my_pharmacy_store.state = "Lagos"
  my_pharmacy_store.postal_code = "102234"
  my_pharmacy_store.country = "Nigeria"
  my_pharmacy_store.latitude = 6.1131  # Replace with actual latitude
  my_pharmacy_store.longitude = 3.311
  my_pharmacy_store.save()
  existing_store = my_pharmacy_store

# Associate the Drug with the PharmacyStore using the many-to-many relationship
existing_store.drugs.append(my_drugs)
my_drugs.save()  # Save the Drug object (updates the association table)

print("-- Drug after association --")
print(my_drugs)

print("-- Reload Drug objects again --")
all_drugs = db.all(Drug)
print("-- Updated Drug objects --")
for obj_id in all_drugs.keys():
  obj = all_drugs[obj_id]
  print(obj)