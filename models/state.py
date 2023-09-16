#!/usr/bin/python3
"""
This is the state class inheriting from the BaseModel parent class
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    This class represents a state where the Airbnb is located
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """This method initialize a State on BaseModel"""
        super().__init__(*args, **kwargs)
