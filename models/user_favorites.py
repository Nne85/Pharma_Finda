#!/usr/bin/python3
""" UserFavorites Class Module """

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref

storage_t = getenv("PHARMACY_Storage")


class UserFavorites(BaseModel, Base):
    """Representation of UserFavorites """
    __tablename__ = 'user_favorites'
    if models.storage_t == ("db"):
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        pharmacy_id = Column(String(60),  ForeignKey('pharmacy_stores.id'), nullable=False)
        favorite_reason = Column(String(256), nullable=True)
        user = relationship("User", back_populates="favorites", overlaps="user_favorites")
        pharmacy = relationship("PharmacyStore")
    else:
        user_id = ""
        pharmacy_id = ""
        favorite_reason = ""

    def __init__(self, *args, **kwargs):
        """initializes UserFavorites"""
        super().__init__(*args, **kwargs)