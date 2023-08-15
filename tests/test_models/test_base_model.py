#!/usr/bin/python3

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_attributes(self):
        self.assertTrue(hasattr(self.base_model, "id"))
        self.assertTrue(hasattr(self.base_model, "created_at"))
        self.assertTrue(hasattr(self.base_model, "updated_at"))

    def test_str_method(self):
        self.assertIn("[BaseModel]", str(self.base_model))
        self.assertIn("id", str(self.base_model))
        self.assertIn("created_at", str(self.base_model))
        self.assertIn("updated_at", str(self.base_model))

    def test_save_method(self):
        prev_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(prev_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        base_model_dict = self.base_model.to_dict()
        self.assertEqual(base_model_dict['__class__'], "BaseModel")
        self.assertIsInstance(base_model_dict['created_at'], str)
        self.assertIsInstance(base_model_dict['updated_at'], str)
        self.assertIsInstance(base_model_dict['id'], str)

if __name__ == '__main__':
    unittest.main()
