import unittest
from models.user import User
from models.base_model import BaseModel
import datetime

class TestUser(unittest.TestCase):

    def test_instance_creation(self):
        """Test creating an instance of User"""
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)

    def test_attributes(self):
        """Test attributes of User class"""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_str_representation(self):
        """Test the __str__ representation"""
        user = User()
        expected = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(str(user), expected)

    def test_email_type(self):
        """Test the type of the 'email' attribute"""
        user = User()
        self.assertIsInstance(user.email, str)

    # Test other attribute types in a similar manner...

    def test_to_dict_method(self):
        """Test the to_dict method"""
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn('__class__', user_dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['id'], user.id)
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()

