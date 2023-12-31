#!/usr/bin/python3
""" This module defines a class to manage file storage for hbnb clone """
import json

class DBStorage:
    """ This class manages storage of hbnb models in JSON format """
    def close(self):
        """ Close the database session """
        self.__session.remove()
