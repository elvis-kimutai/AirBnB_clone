import unittest
from models.review import Review
from models.base_model import BaseModel
import datetime

class TestReview(unittest.TestCase):

    def test_instance_creation(self):
        """Test creating an instance of Review"""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)

    def test_attributes(self):
        """Test attributes of Review class"""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_str_representation(self):
        """Test the __str__ representation"""
        review = Review()
        expected = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(str(review), expected)

    def test_place_id_type(self):
        """Test the type of the 'place_id' attribute"""
        review = Review()
        self.assertIsInstance(review.place_id, str)

    # Test other attribute types in a similar manner...

    def test_to_dict_method(self):
        """Test the to_dict method"""
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertIn('__class__', review_dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['id'], review.id)
        self.assertIsInstance(review_dict['created_at'], str)
        self.assertIsInstance(review_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
