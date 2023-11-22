#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City", backref="state", cascade="all, delete-orphan")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Getter attribute cities that returns the list
            of City instances with state_id equals to the
            current State.id
            """
            from models import storage
            return [city for city in storage.all("City").values()
                    if city.state_id == self.id]
