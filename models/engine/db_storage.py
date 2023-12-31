#!/usr/bin/python3
""" This module defines a class to manage file storage for hbnb clone """
import json

class DBStorage:
    """ This class manages storage of hbnb models in JSON format """
    def close(self):
        """ Close the database session """
        if hasattr(self.__session, 'remove'):
            self.__session.remove()
        elif hasattr(self.__session, 'close'):
            self.__session.close()
