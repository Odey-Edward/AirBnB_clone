#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """FileStorage class that serializes instances to a JSON
    file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = ".".join([obj.__class__.__name__, obj.id])
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        objects = FileStorage.__objects
        obj = {key: objects[key].to_dict() for key in objects}

        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(obj, json_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:

            with open(FileStorage.__file_path, "r") as json_file:
                objects = json.load(json_file)

            for obj in objects.values():
                class_name = obj['__class__']
                del obj['__class__']
                self.new(eval(class_name)(**obj))


        except FileNotFoundError:
            pass
