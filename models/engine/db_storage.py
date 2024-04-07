#!/usr/bin/python3
"""
Contains the class PHARMACY_Storage
"""

import models
from models.base_model import BaseModel, Base
from models.drugs import Drug
from models.users import User
from models. drug_store_inventory import DrugStoreInventory
from models.pharmacy_store import PharmacyStore
from models.user_drugs import UserDrug
from models.user_searches import UserSearches
from models.user_favorites import UserFavorites
from os import getenv
from contextlib import contextmanager
import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Drug": Drug, "PharmacyStore": PharmacyStore,
           "UserSearches": UserSearches, "UserFavorites": UserFavorites,
           "DrugStoreInventory": DrugStoreInventory, "User": User,
           "UserDrug": UserDrug}


class PHARMACY_Storage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        PHARMACY_MYSQL_USER = getenv('PHARMACY_MYSQL_USER')
        PHARMACY_MYSQL_PWD = getenv('PHARMACY_MYSQL_PWD')
        PHARMACY_MYSQL_HOST = getenv('PHARMACY_MYSQL_HOST')
        PHARMACY_MYSQL_DB = getenv('PHARMACY_MYSQL_DB')
        PHARMACY_ENV = getenv('PHARMACY_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(PHARMACY_MYSQL_USER,
                                             PHARMACY_MYSQL_PWD,
                                             PHARMACY_MYSQL_HOST,
                                             PHARMACY_MYSQL_DB))
        if PHARMACY_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """ saves objects to the current database session """
        self.__session.commit()

    def rollback_session(self):
        """ rollback a session """
        self.__session.rollback()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id=None, name=None, email=None):
        """
        get user based on user id passed or  username
        """
        if cls:
            if id:
                obj = self.__session.query(cls).filter_by(id=id).first()
                return obj
            elif name:
                obj = self.__session.query(cls).filter_by(name=name).first()
                return obj
            elif email:
                obj = self.__session.query(cls).filter_by(email=email).first()
                return obj
        else:
            None
    
    def count(self,cls=None):
        """return all object count"""
        objs = self.all(cls)
        return (len(objs))

    @contextmanager
    def session_scope(self):
        """Provide a context manager for session"""
        session = self.__session
        try:
            yield session
            self.__session.commit()
        except Exception as ex:
            self.__session.rollback()
            raise ex
        finally:
            session.close()
