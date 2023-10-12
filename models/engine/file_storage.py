#!/usr/bin/env python3
import json
from datetime import datetime
import copy

class FileStorage():

    __file_path = "file.json"
    __objects = {}

    def all(self):
        os_format = "%Y-%m-%dT%H:%M:%S.%f"
        objects = copy.deepcopy(FileStorage.__objects)

        for key in objects:

            obj_name = objects[key]["__class__"]
            del objects[key]["__class__"]

            objects[key]["created_at"] = datetime.\
                    strptime(objects[key]["created_at"], os_format)
            objects[key]["updated_at"] = datetime.\
                    strptime(objects[key]["updated_at"], os_format)


            objects[key] = '[{}] ({}) {}'.\
                format(obj_name, objects[key]["id"], objects[key])

        return objects

    def new(self, obj):
        key = ".".join([obj.__class__.__name__, obj.id])
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):

        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(FileStorage.__objects, json_file)

    def reload(self):
        try:

            with open(FileStorage.__file_path, "r") as json_file:
                FileStorage.__objects = json.load(json_file)

        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass
