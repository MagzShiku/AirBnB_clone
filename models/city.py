#!/usr/bin/python3
"""
This is a module for the City class """

from models.base_model import BaseModel


class City(BaseModel):
    """
    This class represents a city
    Arguments: integer and string
    """
    state_id = ""
    name = ""
