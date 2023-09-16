#!/usr/bin/python3
"""
This is a module for the place class """

from models.base_model import BaseModel


class Place(BaseModel):
    """
    This is a class that represents a Place
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialize a Place base on BaseModel"""
        super().__init__(self, *args, **kwargs)
