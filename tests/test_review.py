#!/usr/bin/python3
"""
This is a module for the unittests for review.py class
"""
import unittest
from models.engine.file_storage import FileStorage
from models.review import Review  # Import the Review class to be tested


class TestReview(unittest.TestCase):
    """
    This class tests cases for Review class
    """
    def test_review_obj(self):
        """
        This method tests if Review object can be created and its attributes
        are initialized correctly
        """
        item = Review()  # Create an instance of the Review class
        # Check if the attributes of the Review object are
        # initialized correctly
        self.assertEqual(item.text, "")  # Check if 'text' attribute
        # is an empty string
        self.assertEqual(item.place_id, "")  # Check if 'place_id' attribute
        # is an empty string
        self.assertEqual(item.user_id, "")  # Check if 'user_id' attribute is
        # an empty string


if __name__ == "__main__":
    unittest.main()
