#!/usr/bin/python3
from models.engine.db_storage import PHARMACY_Storage
from models.base_model import BaseModel
from models.users import User

db = PHARMACY_Storage()  # Create an instance of the class
db.reload()
all_objs = db.all()

print("-- Reloaded objects --")
for obj_id in all_objs.keys():
  obj = all_objs[obj_id]
  print(obj)

print("-- Create a new User --")
my_user = User()
my_user.name = "Amaka"
my_user.email = "ammy@mail.com"
my_user.search_results = "Panadol"
my_user.password = "root"
my_user.save()
print(my_user)
"""
print("-- Create a new User 2 --")
my_user2 = User()
my_user2.name = "Seun"
my_user2.email = "seunjoko2@mail.com"
my_user2.password = "rootme"
my_user2.save()
print(my_user2)
"""