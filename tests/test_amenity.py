#!/usr/bin/python3
"""
This module defines unit tests for amenity.py
"""

import unittest
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """
    This class tests cases for the Amenity class
    """

    def test_amenity_creation(self):
        """
        This method tests if an Amenity object can be created with a default
        name
        """
        item = Amenity()
        self.assertEqual(item.item, "")

