#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, String


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"

    state_id = Column(String(60), nullable=False, ForeignKey("states.id"))
    name = Column(String(128), nullable=False)

    state = relationship("State", back_populates="cities")
