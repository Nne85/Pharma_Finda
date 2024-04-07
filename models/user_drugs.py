#!/usr/bin/python
""" holds class UserDrug"""
from os import getenv 
from models.base_model import BaseModel, Base
import models
import sqlalchemy
from sqlalchemy import Column, String, DateTime, Text, MetaData, Table,\
    ForeignKey, Integer
from sqlalchemy.orm import relationship, backref
from sqlalchemy.types import Boolean

storage_t = getenv("PHARMACY_Storage")


class UserDrug(BaseModel, Base):
    """Representation of UserDrug """
    __tablename__ = 'user_drugs'
    if models.storage_t == "db":
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        drug_id = Column(String(60), ForeignKey('drugs.id'), nullable=False)

    else:
        user_id = ""
        drug_id = ""

    def __init__(self, *args, **kwargs):
        """initializes UserDrug"""
        super().__init__(*args, **kwargs)