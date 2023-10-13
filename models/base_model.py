#!/usr/bin/python3
"""BaseModel class which all class will inherit from it"""

import uuid
from datetime import datetime
import models

class BaseModel:
    """Define all common attributes and methods
    """
    def __init__(self, *args, **kwargs):
        """Initializes an instance"""
        if kwargs is not None and len(kwargs) != 0:
            if 'class' in kwargs:
                del kwargs['class']
            kwargs['created_at'] = datetime.fromisoformat(kwargs['created_at'])
            kwargs['updated_at'] = datetime.fromisoformat(kwargs['updated_at'])
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()
    def to_dict(self):
        """Return a dictionary representation of instance"""
        my_dict = dict(self.__dict__)
        my_dict.update({'__class__': self.__class__.__name__,
                        'created_at': self.created_at.isoformat(),
                        'id': self.id,
                        'updated_at': self.update_at.isoformat()})
        return my_dict
    
    def __str__(self):
        """String representation"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"