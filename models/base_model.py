#!/usr/bin/python3
""" defines BaseModel class"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """A class that establishes shared features for future classes"""
    def __init__(self, *args, **kwargs):
        """initialization of BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the 'updated_at' attribute"""
        self.updated_at = datetime.now()
        storage.save()
    
    def to_dict(self):
        """converts the instance attributes to a dictionary"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
