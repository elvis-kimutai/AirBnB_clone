import unittest
import os
from models.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Runs before each test"""
        self.storage = FileStorage()

    def tearDown(self):
        """Runs after each test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the all() method"""
        # Create some instances and add them to storage
        bm_instance = BaseModel()
        user_instance = User()
        place_instance = Place()
        state_instance = State()
        city_instance = City()
        amenity_instance = Amenity()
        review_instance = Review()

        self.storage.new(bm_instance)
        self.storage.new(user_instance)
        self.storage.new(place_instance)
        self.storage.new(state_instance)
        self.storage.new(city_instance)
        self.storage.new(amenity_instance)
        self.storage.new(review_instance)

        # Get all instances from storage
        all_instances = self.storage.all()

        # Assert that all instances are in the dictionary
        self.assertIn(bm_instance, all_instances.values())
        self.assertIn(user_instance, all_instances.values())
        self.assertIn(place_instance, all_instances.values())
        self.assertIn(state_instance, all_instances.values())
        self.assertIn(city_instance, all_instances.values())
        self.assertIn(amenity_instance, all_instances.values())
        self.assertIn(review_instance, all_instances.values())

    def test_save_reload(self):
        """Test the save() and reload() methods"""
        # Create an instance, add it to storage, save, and reload
        bm_instance = BaseModel()
        self.storage.new(bm_instance)
        self.storage.save()
        self.storage.reload()

        # Get all instances from reloaded storage
        reloaded_instances = self.storage.all()

        # Assert that the instance is still in the reloaded storage
        self.assertIn(bm_instance, reloaded_instances.values())

if __name__ == '__main__':
    unittest.main()

