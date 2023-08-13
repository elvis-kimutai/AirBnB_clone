import unittest
from models.base_model import BaseModel
import datetime
import models


class TestBaseModel(unittest.TestCase):

    def test_instance_creation(self):
        """Test creating an instance of BaseModel"""
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)

    def test_id_type(self):
        """Test the type of the 'id' attribute"""
        base = BaseModel()
        self.assertIsInstance(base.id, str)

    def test_created_at_type(self):
        """Test the type of the 'created_at' attribute"""
        base = BaseModel()
        self.assertIsInstance(base.created_at, datetime.datetime)

    def test_updated_at_type(self):
        """Test the type of the 'updated_at' attribute"""
        base = BaseModel()
        self.assertIsInstance(base.updated_at, datetime.datetime)

    def test_str_representation(self):
        """Test the __str__ representation"""
        base = BaseModel()
        expected = "[BaseModel] ({}) {}".format(base.id, base.__dict__)
        self.assertEqual(str(base), expected)

    def test_save_method(self):
        """Test the save method"""
        base = BaseModel()
        original_updated_at = base.updated_at
        base.save()
        self.assertNotEqual(base.updated_at, original_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertIn('__class__', base_dict)
        self.assertEqual(base_dict['__class__'], 'BaseModel')
        self.assertEqual(base_dict['id'], base.id)
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()

