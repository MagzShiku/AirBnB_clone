#!/usr/bin/python3
"""
This is a module that defines unit tests for the base_model.py
"""
from unittest import TestCase
from datetime import datetime
from models.base_model import BaseModel
from unittest import mock

BaseModel = base_model.BaseModel


class TestBase(unittest.TestCase):
    """
    This is the TestBase class, a subclass in the unittest
    that contains the individual test methods
    """

    def test_init(self):
        """
        This is the initializer method
        """

        self.assertIsInstance(self.base, BaseModel)

    def SetUp(self):
        """
        This is the method that sets the instance
        for class tests
        """
        self.base = BaseModel()

    def test_init_attr(self):
        """
        This is a method that tests if the initial attributes are set up
        """
        base_list = ['id', 'created_at', 'updated_at']
        base_str = str(self.base)
        i = 0
        for item in base_list:
            if item in base_str:
                i += 1
        self.assertEqual(3, count)  # fix the int later

    def test_kwargs(self):
        """
        This method test for attributes passed by keys and their valules
        """
        base_kwargs = BaseModel(name="Test_Model", number=60)  # fix the int
        dict_base_kwargs = base_kwargs.to_dict()
        test_attr = ['name', 'number', 'created_at', 'updated_at', '__class__']
        real_attr = list(dict_base_kwargs.keys())
        self.assertCountEqual(real_attr, test_attr)

    def test_class_attr(self):
        """
        This method tests a class attribute passed as a key and value(kwargs)
        """

        base_class = BaseModel(__class__='Test', id="")  # fix the id later
        self.assertEqual(type(base_class), BaseModel)

    @mock.patch('models.storage')  # This decorater mocks some parts of the
    # code, allowing the tests to isolate and focus on specific functionality
    def test_to_dict(self):
        """
        This method tests the dictionary conversion and creates new
        key vakue pairs
        """

        self.base.name = 'Test_Model'
        self.base.number = 60
        dict_test = self.base.to_dict()
        test_attr = ['id', 'name', 'number', 'created_at', 'updated_at',
                     '__class__']
        real attr = list(dict_test.keys())
        self.assertCountEqual(real_attr, test_attr)

    def test_save(self, mock_engine):
        """
        This is a method that that tests base save method without
        models.storage method
        """

        init_updated_at = self.base.updated_at
        self.base.save()
        last_updated_at = self.base.updated_at
        self.assertNotEqual(init_updated_at, last_updated_at)
        self.assertTrue(mock_engine.save.called)

    def test_str(self):
        """
        Thisis a method that tests the string method
        """
        test_str = f"[BaseModel] ({self.base.id}) {self,base.__dict__}"
        self.assertEqual(test_str, str(self.base))

    def test_to_dict_values(self):
        """
        This is a method that that tests the dict values
        """

        self.base.name = 'Test_Model'
        self.base.number = 60
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        dict_test = self.base.to_dict()
        self.assertEqual(dict_test['name'], 'Test_Model')
        self.assertEqual(dict_test['number'], 60)  # fix this number later
        self.assertEqual(dict_test['__class__'], 'BaseModel')
        self.assertEqual(dict_test['created_at']
                         self.base.created_at.strftime(time_format))
        self.assertEqual(dict_test['updated_at']
                         self.base.updated_at.strftime(time_format))


if __name__ == '__main__':
    unittest.main()
# ensures that the tests run only when the script is executed directly
# not when it is imported
