#!/usr/bin/python3
"""
This is a module unit that tests for place.py class
"""

import unittest
from models.place import Place
from models.engine.file_storage import FileStorage


class TestPlace(unittest.TestCase):
    """
    This class tests unit cases for the Place class
    """

    def test_place_creation(self):
        """
        This method tests if a Place object can be created with default values
        """
        item = Place()
        self.assertEqual(item.city_id, "")
        self.assertEqual(item.user_id, "")
        self.assertEqual(item.name, "")
        self.assertEqual(item.description, "")
        self.assertEqual(item.number_bathrooms, 0)
        self.assertEqual(item.number_rooms, 0)
        self.assertEqual(item.max_guest, 0)
        self.assertEqual(item.price_by_night, 0)
        self.assertEqual(item.latitude, 0.0)
        self.assertEqual(item.longitude, 0.0)
        self.assertEqual(item.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
