import unittest
from models.state import State
from models.base_model import BaseModel
import datetime

class TestState(unittest.TestCase):

    def test_instance_creation(self):
        """Test creating an instance of State"""
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)

    def test_attributes(self):
        """Test attributes of State class"""
        state = State()
        self.assertTrue(hasattr(state, 'name'))

    def test_str_representation(self):
        """Test the __str__ representation"""
        state = State()
        expected = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(str(state), expected)

    def test_name_type(self):
        """Test the type of the 'name' attribute"""
        state = State()
        self.assertIsInstance(state.name, str)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIn('__class__', state_dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['id'], state.id)
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()

