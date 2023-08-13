#!/usr/bin/python
""" Define the class User"""

from models.base_model import BaseModel

class User(BaseModel):
    """ the class user  """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
