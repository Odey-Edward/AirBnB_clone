#!/usr/bin/python3
"""base_model module"""
import uuid
from datetime import datetime


class BaseModel:
    """Define BaseModel class"""

    def __init__(self) -> None:
        """initialize instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        """returns the string representation of class"""
        return '[{}] ({}) {}'.\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
            updates the public instance attribute updated at
            with the current datetime.
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
            returns a dictionary containing all key/values of
            __dict__ of the instance
        """

        new_dict = dict(self.__dict__)
        new_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        new_dict['created_at'] = self.__dict__['created_at'].isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
