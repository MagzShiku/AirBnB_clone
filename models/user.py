#!usr/bin/python3
"""
This is a module defining classes in the application that inherit from
base model
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    This is the class that represents a user with attributes such as
    email, password, first_name, last_name as CLI arguments
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
