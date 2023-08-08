#!/usr/bin/python3
"""
The module defines BaseModel class
"""

import uuid
from datetime import datetime

class BaseModel:
    """
    A class that establishes shared features for future classes
    """
    def __init__(self, *args, **kwargs):
        """
        initialization of BaseModel
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        String representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates 'updated_at' attribute with current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the instance to a dictionary representation
        Returns: dictionary containing keys and values of __dict__
        """
        objdict = self.__dict__.copy()
        objdict['__class__'] = self.__class__.__name__
        objdict['created_at'] = self.created_at.isoformat()
        objdict['updated_at'] = self.updated_at.isoformat()
        return objdict
