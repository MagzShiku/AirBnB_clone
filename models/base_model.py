#!/usr/bin/python3
"""
this is a base model. It defines all common attributes/methods
for other classes
"""


from datetime import datetime
import uuid

class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        generate a unique id usin uuid.uuid4()
        -> You can use uuid.uuid4() to generate unique id but don’t
        forget to convert to a string.
        -> The goal is to have unique id for each BaseModel
        """

        """We are updating the init method to re-create an instance
        with this dictionary representation
        """

        if kwargs:
            # iterate ove the key_value pairs in kwargs
            for key, value in kwargs.items():
                
                # skip the __class__ attribute
                if key == '__class__':
                    continue
                # convert the created and updated intp datetime objects
                # this helps them be easier to work with and
                # compatible with program
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                
                # set the attribute on the instance
                setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())

            # set the created_at attribute to the current datetime
            self.created_at = datetime.now()

            # set the updated_at attribute to the same value as the created at
            self.updated_at = self.created_at

    def __str__(self):
        """
        return a string representation of the instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                self.__dict__)

    def save(self):
        """
        update the 'updated' attribute to the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        creating a copy of the dictionary of the attributes of the instance
        attr_dict is the data for the created at and the updated at attr
        """
        attr_dict = self.__dict__.copy()

        # add the class name to dictionary
        attr_dict['__class__'] = self.__class__.__name__

        # convert the created func into ISO format and update the dict
        # ISO format for date is 'YYYY-MM-DD' and for time is 'HH:MM:SS'
        attr_dict['created_at'] = self.created_at.isoformat()

        # we do the same for 'updated_at' for attribute for the instance
        attr_dict['updated_at'] = self.updated_at.isoformat()

        # now we return dictionary with updated data... attr_dict
        return attr_dict
