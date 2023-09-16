#!/usr/bin/python3
"""
This is a base model module. It defines all common attributes/methods
for other classes
"""

from datetime import datetime
import uuid
from models import storage

classes = {}

class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        This method generate a unique id using uuid.uuid4()
        -> You can use uuid.uuid4() to generate unique id but don’t
        forget to convert to a string.
        -> The goal is to have unique id for each BaseModel
        """

        """
        We are updating the init method to re-create an instance
        with this dictionary representation
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
        """
        short_form = self.__class__.__name__
        return "[{}] ({}) {}".format(short_form, self.id, self.__dict__)

    def save(self):
        """
        This save method saves the 'updated' attribute to the current datetime
        """
        self.updated_at = datetime.now()
        # this ises the storage method
        storage.save()

    def to_dict(self):
        """
        This method is creating a copy of the dictionary of the
        attributes of the instance attr_dict is the data for the
        created at and the updated at attr
        """
        attr_dict = self.__dict__.copy()

        # add the class name to dictionary
        attr_dict['__class__'] = self.__class__.__name__

        # convert the created func into ISO format and update the dict
        # ISO format for date is 'YYYY-MM-DD' and for time is 'HH:MM:SS'
        # we do the same for 'updated_at' for attribute for the instance
        attr_dict['created_at'] = self.created_at.isoformat()
        attr_dict['updated_at'] = self.updated_at.isoformat()

        # now we return dictionary with updated data... attr_dict
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
#print(base_model_dict)
