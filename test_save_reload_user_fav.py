#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user_favorites import UserFavorites


all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new UserFavorites 2 --")
my_userfav = UserFavorites()
my_userfav.favorite_reason = ""
my_userfav.save()
print(my_userfav)

print("-- Create a new UserFavorites 2 --")
my_userfav = UserFavorites()
my_userfav.favorite_reason = ""
my_userfav.save()
print(my_userfav)
