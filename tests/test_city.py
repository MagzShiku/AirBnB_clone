#!/usr/bin/python3
"""
This is the module unit tests for city.py
"""

import unittest
from models.city import City
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
    """
    This class tests cases for the City class
    """

    def test_city_creation(self):
        """
        This method tests if a City object can be created with default values
        """
        item = City()
        self.assertEqual(item.name, "")
        self.assertEqual(item.state_id, "")


if __name__ == "__main__":
    unittest.main()
