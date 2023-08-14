#!/usr/bin/pyton3

import unittest
from unittest.mock import patch
from io import StringIO
import os
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_quit_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(mock_stdout.getvalue().strip(), "")

    def test_EOF_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual(mock_stdout.getvalue().strip(), "")

    def test_create_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create User")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)  # Length of UUID
            self.assertTrue(output.isalnum())

    def test_show_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("show User")
            self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")

            self.console.onecmd("create User")
            output = mock_stdout.getvalue().strip()
            instance_id = output.split()[-1]

            mock_stdout.truncate(0)  # Clear the mock_stdout buffer
            self.console.onecmd(f"show User {instance_id}")
            self.assertIn("User", mock_stdout.getvalue())

    
    def test_destroy_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("destroy User")
            self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")

            self.console.onecmd("create User")
            output = mock_stdout.getvalue().strip()
            instance_id = output.split()[-1]

            mock_stdout.truncate(0)  # Clear the mock_stdout buffer
            self.console.onecmd(f"destroy User {instance_id}")
            self.assertEqual(mock_stdout.getvalue().strip(), "")

    def test_all_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("all User")
            self.assertEqual(mock_stdout.getvalue().strip(), "")

            self.console.onecmd("create User")
            self.console.onecmd("create User")
            self.console.onecmd("create Place")
            self.console.onecmd("all User")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(len(output.split("\n")), 2)  # Should have 2 User instances

    def test_update_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("update User")
            self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")

            self.console.onecmd("create User")
            output = mock_stdout.getvalue().strip()
            instance_id = output.split()[-1]

            self.console.onecmd(f"update User {instance_id} name John")
            self.assertEqual(mock_stdout.getvalue().strip(), "** attribute name missing **")

            self.console.onecmd(f"update User {instance_id} first_name John")
            self.console.onecmd(f"show User {instance_id}")
            self.assertIn("John", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
