#!/usr/bin/python3
"""
This module Unit defines Test Module for User Class
"""
import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """
    This class contains tests for User Model
    """

    def test_init_no_args(self):
        """
        This method tests instance creation with no arguments
        """
        # Create a User instance with no arguments
        user_instance = User()
        # Define a list of expected attribute names
        expected_attrs = [
            'id', 'created_at',
            'updated_at', '__class__'
        ]
        # Get the attribute names of the User instance and store them in
        # attr_names
        attr_names = list(user_instance.to_dict().keys())
        # Assert that the attribute names match the expected ones
        self.assertEqual(attr_names, expected_attrs)

    def test_init_kwargs_args(self):
        """
        This method tests instance creation with keyword arguments
        """
        # Create a User instance with keyword arguments
        user_instance = User(name='Magdalene', age="30", time='now')
        # Define a list of expected attribute names
        expected_attrs = [
            'id', 'created_at', 'updated_at',
            'name', 'age', 'time', '__class__'
        ]
        # Get the attribute names of the User instance and store them in
        # attr_names
        attr_names = list(user_instance.to_dict().keys())
        # Assert that the attribute names match the expected ones
        self.assertEqual(attr_names, expected_attrs)

    def test_init_args_args(self):
        """
        This method tests instance creation with positional arguments
        """
        # Create a User instance with positional arguments
        user_instance = User(22, "new", "good tidings", 60)
        # Define a list of expected attribute names
        expected_attrs = [
            'id', 'created_at',
            'updated_at', '__class__'
        ]
        # Get the attribute names of the User instance and store them in
        # attr_names
        attr_names = list(user_instance.to_dict().keys())
        # Assert that the attribute names match the expected ones
        self.assertEqual(attr_names, expected_attrs)

    def test_init_args_and_kwargs(self):
        """
        This method tests instance creation with both positional and
        keyword arguments
        """
        # Create a User instance with both positional and keyword arguments
        user_instance = User("Jenna", "new", "28", name="Moore", age=30)
        # Define a list of expected attribute names
        expected_attrs = [
            'id', 'created_at', 'updated_at',
            'name', 'age', '__class__'
        ]
        # Get the attribute names of the User instance and store them in
        # attr_names
        attr_names = list(user_instance.to_dict().keys())
        # Assert that the attribute names match the expected ones
        self.assertEqual(attr_names, expected_attrs)

    def test_str_representation(self):
        """
        This method tests the string representation of a User instance
        """
        # Create a User instance
        user_instance = User()
        # Get the name of the User instance's class
        class_name = type(user_instance).__name__
        # Get the id attribute of the User instance
        user_id = user_instance.id
        # Get the dictionary representation of the User instance
        user_dict = str(user_instance.__dict__)
        # Define the expected string representation
        expected_output = "[{}] ({}) {}".format(class_name, user_id, user_dict)
        # Assert that the generated string matches the expected one
        self.assertEqual(str(user_instance), expected_output)

    def test_default_attributes(self):
        """
        This method tests default values of class attributes
        """
        # Create a User instance
        user_instance = User()
        # Check the default values of email, password, first_name, and
        # last_name attributes
        self.assertEqual(user_instance.email, "")
        self.assertEqual(user_instance.password, "")
        self.assertEqual(user_instance.first_name, "")
        self.assertEqual(user_instance.last_name, "")


if __name__ == '__main__':
    unittest.main()
