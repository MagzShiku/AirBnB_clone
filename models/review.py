#!/usr/bin/python3
"""
This is a module for the review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    This is a class that represents a Review of the airbnb services
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """This method initialize a Review base on BaseModel"""
        super().__init__(self, *args, **kwargs)
