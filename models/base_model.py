#!/usr/bin/python3
"""
This is a base model module. It defines all common attributes/methods
for other classes
"""

from datetime import datetime
import uuid
from models import storage

classes = {}
"""
this is an empty directory that will have collection of all key, value pairs
it'll be imported by concole.py
"""


class BaseModel:
    """
    This is the maon base model for the project, the other classes will be calling this
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class with the provided arguments.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Note:
            - This method generates a unique ID using uuid.uuid4().
            - The generated ID is converted to a string for storage.

        Returns:
            None

        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if kwargs:
            storage.new(self)
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)

    def __str__(self):
        """
        This method returns a string representation of the instance

        Returns:
            str: A string representation of the instance.
        """
        short_form = self.__class__.__name__
        return "[{}] ({}) {}".format(short_form, self.id, self.__dict__)

    def save(self):
        """
        This save method saves the 'updated' attribute to the current datetime

        Returns:
            None
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        This method is creating a copy of the dictionary of the
        attributes of the instance attr_dict is the data for the
        created at and the updated at attr

        Returns:
            dict: A dictionary representation of the instance attributes.
        """
        attr_dict = self.__dict__.copy()

        attr_dict['__class__'] = self.__class__.__name__
        attr_dict['created_at'] = self.created_at.isoformat()
        attr_dict['updated_at'] = self.updated_at.isoformat()

        return attr_dict


"""
Create an instance of the BaseModel class
"""
base_model = BaseModel(my_number=89, name="My_First_Model")

"""
Call the to_dict() method to convert the instance attributes to a dictionary
"""

base_model_dict = base_model.to_dict()

# print the directory representation
# print(base_model_dict)
