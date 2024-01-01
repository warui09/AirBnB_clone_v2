#!/usr/bin/python3
""" This module defines a class to manage file storage for hbnb clone """

from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database connection"""
        self.__engine = create_engine(
            "mysql://holberton_user:projectcorrection280hbtn@55.89.49.53:3306/tyrell_corp",
            pool_pre_ping=True,
        )
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        result_dict = {}

        if cls:
            objects = self.__session.query(cls).all()
        else:
            objects = []
            for model_class in Base._decl_class_registry.values():
                if hasattr(model_class, "__table__"):
                    objects.extend(self.__session.query(model_class).all())

        for obj in objects:
            key = f"{obj.__class__.__name__}.{obj.id}"
            result_dict[key] = obj

        return result_dict

    def new(self, obj):
        """Adds new object to storage session"""
        self.__session.add(obj)

    def save(self):
        """Saves storage session changes to the database"""
        self.__session.commit()

    def reload(self):
        """Reloads storage session from the database"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def delete(self, obj=None):
        """Delete an object from the storage session"""
        if obj:
            self.__session.delete(obj)

    def close(self):
        """Close the database session"""
        self.__session.close()
