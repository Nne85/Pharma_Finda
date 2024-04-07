#!/usr/bin/python
""" holds class PharmacyStore"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import uuid
from sqlalchemy import Column, String, Float, ForeignKey, DateTime, Index
from sqlalchemy.orm import relationship, backref

storage_t = getenv("PHARMACY_Storage")


class PharmacyStore(BaseModel, Base):
    """Representation of PharmacyStore """
    __tablename__ = 'pharmacy_stores'
    if models.storage_t == ("db"):
        name = Column(String(128), nullable=False)
        address = Column(String(1024), nullable=False)
        city = Column(String(60), nullable=False)
        state = Column(String(60), nullable=False)
        postal_code = Column(String(20), nullable=False)
        country = Column(String(128), nullable=False)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        inventory = relationship('DrugStoreInventory', backref='pharmacy_store', overlaps="pharmacy")
        drugs = relationship("Drug", back_populates="pharmacy_stores",
                             secondary="pharmacy_stores_drugs")
    else:
        name = ""
        address = ""
        city = ""
        state = ""
        postal_code = ""
        country = ""
        latitude = ""
        longitude = ""

    def __init__(self, *args, **kwargs):
        """initializes PharmacyStore"""
        super().__init__(*args, **kwargs)

    def list_drugs(self):
        """Returns a list of Drug instances associated with the store"""
        return self.drugs