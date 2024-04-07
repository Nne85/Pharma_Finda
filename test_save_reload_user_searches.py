#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user_searches import UserSearches

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new UserSearches 1 --")
my_usersearch = UserSearches()
my_usesearch.search_results = ""
my_usersearch.search_date = datetime.datetime.now()
my_usersearch.save()
print(my_usersearch)

print("-- Create a new UserSeaches 2 --")
my_usersearch = UserSearches()
my_usersearch.search_results = ""
my_usersearch.search_date = datetime.datetime.now()
my_usersearch.save()
print(my_usersearch)
