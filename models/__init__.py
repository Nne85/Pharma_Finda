#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv


storage_t = getenv("PHARMACY_Storage")

if storage_t == "db":
    from models.engine.db_storage import PHARMACY_Storage
    storage = PHARMACY_Storage()
    storage.reload()
else:
    print("Error conecting to database")
    """from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()"""
