#!/usr/bin/python3
"""
This module contains Unittests for state.py class
"""
import unittest
from models.engine.file_storage import FileStorage
from models.state import State  # Import the State class to be tested

class TestState(unittest.TestCase):
    """
    This class tests cases for State class
    """
    def test_state_obj(self):
        """
        This method tests if State object can be created and its
        attribute is initialized correctly
        """
        item = State()  # Create an instance of the State class
        # Check if the 'name' attribute of the State object is
        # initialized correctly
        self.assertEqual(item.name, "")


if __name__ == "__main__":
    unittest.main()
