import unittest
import os
import sys
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class TestConsole(unittest.TestCase):

    def setUp(self):
        """Runs before each test"""
        self.console = HBNBCommand()
        sys.stdout = StringIO()  # Redirect stdout for testing

    def tearDown(self):
        """Runs after each test"""
        sys.stdout = sys.__stdout__  # Restore stdout

    def test_quit(self):
        """Test the quit command"""
        self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Test the EOF command"""
        self.assertTrue(self.console.onecmd("EOF"))

    def test_create(self):
        """Test the create command"""
        self.console.onecmd("create BaseModel")
        output = sys.stdout.getvalue().strip()
        self.assertTrue(output.isalnum())  # Check if ID is alphanumeric

    def test_show(self):
        """Test the show command"""
        bm = BaseModel()
        bm_id = bm.id
        self.console.onecmd("show BaseModel {}".format(bm_id))
        output = sys.stdout.getvalue().strip()
        self.assertIn(bm_id, output)  # Check if ID is present in output

    def test_all(self):
        """Test the all command"""
        bm = BaseModel()
        self.console.onecmd("all BaseModel")
        output = sys.stdout.getvalue().strip()
        self.assertIn(str(bm), output)  # Check if BaseModel is in output

    # Add more test methods for other commands as needed

if __name__ == '__main__':
    unittest.main()

