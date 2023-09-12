#!/usr/bin/python3
"""
This is a base model module. It defines all common attributes/methods
for other classes
"""


from datetime import datetime
import uuid

class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        This method generate a unique id using uuid.uuid4()
        -> You can use uuid.uuid4() to generate unique id but don’t
        forget to convert to a string.
        -> The goal is to have unique id for each BaseModel
        """

        """We are updating the init method to re-create an instance
        with this dictionary representation
        """

        if kwargs:
            # Iterate over the key_value pairs in kwargs
            for key, value in kwargs.items():
                
                # skip the __class__ attribute
                if key == '__class__':
                    continue
                # Convert the created and updated datetime objects
                # This helps them be easier to work with and
                # compatible with the program
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                # The datetime.strptime() method returns a datetime object
                # that matches the date_string parsed by the format
                
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
        This method returns a string representation of the instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                self.__dict__)

    def save(self):
        """
        This save method saves the 'updated' attribute to the current datetime
        """
        self.updated_at = datetime.now()

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
        attr_dict['created_at'] = self.created_at.isoformat()

        # we do the same for 'updated_at' for attribute for the instance
        attr_dict['updated_at'] = self.updated_at.isoformat()

        # now we return dictionary with updated data... attr_dict
        return attr_dict