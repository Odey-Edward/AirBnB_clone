#!/usr/bin/python3
"""base_model module"""
from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    """Define BaseModel class"""

    def __init__(self, *args, **kwargs) -> None:
        """initialize instance"""
        IsoFormat = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                if key == "created_at":
                    self.created_at = datetime.strptime(kwargs[key], IsoFormat)
                if key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs[key], IsoFormat)
        elif args:
            storage.new(self)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

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
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all key/values of
            __dict__ of the instance
        """
        obj_dict = dict(self.__dict__)

        obj_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        obj_dict['created_at'] = self.__dict__['created_at'].isoformat()
        obj_dict['__class__'] = self.__class__.__name__

        return obj_dict
