#!/usr/bin/python3

"""serialization and deserialization of instances"""

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os
import json


class FileStorage:
    """serialize and deserialize"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return dictionary of objects"""
        return (self.__objects)

    def new(self, obj):
        """sets objs with keys"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """serializes objs to json files"""
        with open(self.__file_path,"w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """deserializes json file to obj"""
        try:
            with open(self.__file_path, "r") as f:
                data = f.read()
                if data:
                    self.__objects = json.loads(data)
        except FileNotFoundError:
            pass