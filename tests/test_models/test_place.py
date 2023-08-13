import unittest
from models.place import Place
from models.base_model import BaseModel
import datetime

class TestPlace(unittest.TestCase):

    def test_instance_creation(self):
        """Test creating an instance of Place"""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)

    def test_attributes(self):
        """Test attributes of Place class"""
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))

    def test_str_representation(self):
        """Test the __str__ representation"""
        place = Place()
        expected = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(str(place), expected)

    def test_city_id_type(self):
        """Test the type of the 'city_id' attribute"""
        place = Place()
        self.assertIsInstance(place.city_id, str)

    # Test other attribute types in a similar manner...

    def test_to_dict_method(self):
        """Test the to_dict method"""
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertIn('__class__', place_dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['id'], place.id)
        self.assertIsInstance(place_dict['created_at'], str)
        self.assertIsInstance(place_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()

