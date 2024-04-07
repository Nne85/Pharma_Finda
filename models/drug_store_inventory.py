#!/usr/bin/python
""" holds class DrugStoreInventory"""

from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey,\
    MetaData, Table, Index
from sqlalchemy.orm import relationship, backref

storage_t = getenv("PHARMACY_Storage")


class DrugStoreInventory(BaseModel, Base):
    """Representation of DrugStoreInventory """
    __tablename__ = 'drug_store_inventory'
    if models.storage_t == "db":
        pharmacy_id = Column(String(60), ForeignKey('pharmacy_stores.id'), nullable=False)
        drug_id = Column(String(60), ForeignKey('drugs.id'), nullable=False)
        stock_quantity = Column(Integer, nullable=False)
        drug = relationship("Drug")
        pharmacy = relationship("PharmacyStore", back_populates="inventory", overlaps="pharmacy")
    
    else:
        pharmacy_id = ""
        drug_id = ""
        stock_quantity = ""

    def __init__(self, *args, **kwargs):
        """initializes DrugStoreInventory"""
        super().__init__(*args, **kwargs)