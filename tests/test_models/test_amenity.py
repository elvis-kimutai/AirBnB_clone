#!/usr/bin/python3
"""Defines unittests for models/amenity.py.
Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)

class TestAmenity(unittest.TestCase):

    def test_instance_creation(self):
        """Test creating an instance of Amenity"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

    def test_attribute_default_values(self):
        """Test default values of attributes"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

if __name__ == '__main__':
    unittest.main()
