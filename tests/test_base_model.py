#!/usr/bin/python3
"""
This is a module that defines the BaseModel class
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
import os


class TestBaseModel(unittest.TestCase):
    """
    Test class for the BaseModel class
    """

    def setUp(self):
        """
        Set up a fresh BaseModel instance for each test.
        """
        self.base_model = BaseModel()

    def tearDown(self):
        """
        Clean up resources after each test if necessary.
        """
        del self.base_model
        # Optionally, you can remove the 'file.json' created during testing.
        if os.path.isfile("file.json"):
            os.remove("file.json")

    def test_save(self):
        """
        Test the save method of BaseModel.
        """
        created_at = self.base_model.created_at
        self.base_model.save()
        updated_at = self.base_model.updated_at

    def test_to_dict(self):
        """
        Test the to_dict method of BaseModel.
        """
        obj_dict = self.base_model.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)

        # You can also check if the keys are present or not if needed.
        self.assertIn("id", obj_dict)


if __name__ == '__main__':
    unittest.main()
