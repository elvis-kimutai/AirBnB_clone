import unittest
from models.city import City
from models.base_model import BaseModel
import datetime

class TestCity(unittest.TestCase):

    def test_instance_creation(self):
        """Test creating an instance of City"""
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)

    def test_state_id_type(self):
        """Test the type of the 'state_id' attribute"""
        city = City()
        self.assertIsInstance(city.state_id, str)

    def test_name_type(self):
        """Test the type of the 'name' attribute"""
        city = City()
        self.assertIsInstance(city.name, str)

    def test_str_representation(self):
        """Test the __str__ representation"""
        city = City()
        expected = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(str(city), expected)

    def test_city_attributes(self):
        """Test attributes of City class"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_to_dict_method(self):
        """Test the to_dict method"""
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertIn('__class__', city_dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['id'], city.id)
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()

