"""User Class Module"""

from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, Integer,\
    MetaData, Table, ForeignKey, Boolean
from hashlib import md5
from sqlalchemy.orm import relationship, backref

storage_t = getenv("PHARMACY_Storage")


class User(BaseModel, Base):
    """Representation of User """
    __tablename__ = 'users'
    if models.storage_t == ("db"):
        name = Column(String(128), nullable=False)
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        location = Column(String(1024), nullable=False)
        searches = relationship("UserSearches", backref="user")
        favorites = relationship("UserFavorites", backref='user_favorites')
        search_results = Column(String(512), nullable=True)

    else:
        name = ""
        email = ""
        password = ""
        searches = ""
        favorites = ""
        search_results = ""

    def __init__(self, *args, **kwargs):
        """initializes User"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
