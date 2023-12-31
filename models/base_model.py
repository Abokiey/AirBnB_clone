#!/usr/bin/python3

"""basemodel for airbnb"""

from copy import deepcopy
import uuid
from datetime import datetime
import models


class BaseModel:
    """the base class of the project"""
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        date_format = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value, date_format)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, date_format)

                elif key == "__class__":
                    pass

                else:
                    self.__dict__[key] = value

        else:
            models.storage.new(self)

    def __str__(self):
        """string rpresentation"""
        return ("[{}] ({}) {}".format
                (self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the updated_at"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """dictionary containing all keys/values of __dict__"""
        obj = deepcopy(self.__dict__)
        obj["__class__"] = self.__class__.__name__
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()

        return (obj)
