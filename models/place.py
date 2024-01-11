#!/usr/bin/python3
"""Place Class"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Place that inherits from Base"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = int()
    number_bathrooms = int()
    max_guest = int()
    price_by_night = int()
    latitude = float()
    longitude = float()
    amenity_ids = []
