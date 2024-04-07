#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.drug_store_inventory import DrugStoreInventory

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new DrugStoreInventory 1 --")
my_druginventory = DrugStoreInventory()
my_druginventory.stock_quantity = 12
my_druginventory.save()
print(my_druginventory)

print("-- Create a new DrugStoreInventory 2 --")
my_druginventory = DrugStoreInventory()
my_druginventory.stock_quantity = 15
my_druginventory.save()
print(my_druginventory)
