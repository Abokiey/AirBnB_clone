#!/usr/bin/python3
"""
Filestorage class module
"""

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import datetime

class FileStorage:
    """
    Class that seralizes instance to a JSON file and deserializes JSON
    file to instance:
    Attributes:
        [Class attribute]
        __file_path (string): path to the JSON file (ex: file.json)
        __objects (dict): empty but will store all objects by <class name>.id
        
        [instance methods]
        all(self): return the dictionary __objects
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary __objects
        """
        return FileStorage.__objects
    def new(self, obj):
        """
        sets in __objects obj with key <obj_class_name>.id
        """
        class_name = obj.__class__.__name__
        id_ = obj.id
        format_ = "{}.{}".format(class_name, id)
        FileStorage.__objects[format] = obj
    def save(self):
        """
        Serializes __objects to the JSON file __file_path
        """
        data = FileStorage.__objects
        objects_to_dict = {obj: data[obj].to_dict() for obj in data.keys()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            file.write(json.dumps(objects_to_dict))
    def reload(self):
        """
        Deserializes the JSON file __file_path to __objects, if it exists
        the 'eval()' fuction process a string like a normal command and
        return the output
        => a = "print('hello')" <---> [string]
        => eval(a) returns "hello"
        """
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as f:
                objdict = json.load(f)
                for obj in objdict.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return