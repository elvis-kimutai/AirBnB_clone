#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.user = User()
        self.place = Place()
        self.state = State()
        self.city = City()
        self.amenity = Amenity()
        self.review = Review()

    def test_all_method(self):
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new_method(self):
        key = "{}.{}".format(self.base_model.__class__.__name__, self.base_model.id)
        self.storage.new(self.base_model)
        self.assertTrue(key in self.storage.all())

    def test_save_method(self):
        key = "{}.{}".format(self.user.__class__.__name__, self.user.id)
        self.storage.new(self.user)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r') as file:
            data = file.read()
            self.assertTrue(key in data)

    def test_reload_method(self):
        key = "{}.{}".format(self.place.__class__.__name__, self.place.id)
        self.storage.new(self.place)
        self.storage.save()
        self.storage.reload()
        self.assertTrue(key in self.storage.all())

    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass

if __name__ == '__main__':
    unittest.main()
