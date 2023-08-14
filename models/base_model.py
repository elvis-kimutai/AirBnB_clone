#!/usr/bin/python3
"""Defines BaseModel class"""

import uuid
from datetime import datetime
import models

class BaseModel:
    """A class that establishes shared features for future classes"""
    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns the string representation of the instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the attribute and saves the instance"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Converts the instance to a dictionary"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
