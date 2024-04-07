#!/usr/bin/python3
from models.engine.db_storage import PHARMACY_Storage
from models.base_model import BaseModel
from models.pharmacy_store import PharmacyStore
import uuid

db = PHARMACY_Storage()  # Create an instance of the storage class
db.reload()  # Connect to the database

all_objs = db.all(PharmacyStore)  # Retrieve all PharmacyStore objects

print("-- Reloaded PharmacyStore objects --")
for obj_id in all_objs.keys():
  obj = all_objs[obj_id]
  print(obj)

print("-- Create a new PharmacyStore --")
my_pharmacy_store = PharmacyStore()
my_pharmacy_store.store_id = "eeb6da99-3b07-4e7d-a0b6-9b0812617324"
my_pharmacy_store.name = "LanYard Pharmacy"
my_pharmacy_store.address = "Ago Palace Way"
my_pharmacy_store.city = "Isolo"
my_pharmacy_store.state = "Lagos"
my_pharmacy_store.postal_code = "12222"
my_pharmacy_store.country = "Nigeria"
my_pharmacy_store.latitude = 12.2224  # Replace with actual latitude
my_pharmacy_store.longitude = -13.0864  # Replace with actual longitude
my_pharmacy_store.save()  # Save the new pharmacy store
print(my_pharmacy_store)

print("-- Reload PharmacyStore objects again --")
all_objs = db.all(PharmacyStore)
print("-- Updated PharmacyStore objects --")
for obj_id in all_objs.keys():
  obj = all_objs[obj_id]
  print(obj)