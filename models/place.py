#!/usr/bin/python3
"""Place Class"""

from models.base_model import BaseModel


class Place(BaseModel):

    """Place class for AirBnB project.

    Attributes:
        city_id (str): The city ID associated with the place.
        user_id (str): The user ID associated with the place.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests allowed.
        price_by_night (int): The price per night for the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): List of amenity IDs associated with the place.
    """
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

    def __init__(self, *args, **kwargs):
        """Initializes a new Place instance.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)

        if 'city_id' in kwargs and kwargs['city_id']:
            self.city_id = kwargs['city_id']
        if 'user_id' in kwargs and kwargs['user_id']:
            self.user_id = kwargs['user_id']
        if 'name' in kwargs and kwargs['name']:
            self.name = kwargs['name']
        if 'description' in kwargs and kwargs['description']:
            self.description = kwargs['description']
        if 'number_rooms' in kwargs and kwargs['number_rooms']:
            self.number_rooms = kwargs['number_rooms']
        if 'number_bathrooms' in kwargs and kwargs['number_bathrooms']:
            self.number_bathrooms = kwargs['number_bathrooms']
        if 'max_guest' in kwargs and kwargs['max_guest']:
            self.max_guest = kwargs['max_guest']
        if 'price_by_night' in kwargs and kwargs['price_by_night']:
            self.price_by_night = kwargs['price_by_night']
        if 'latitude' in kwargs and kwargs['latitude']:
            self.latitude = kwargs['latitude']
        if 'longitude' in kwargs and kwargs['longitude']:
            self.longitude = kwargs['longitude']
        if 'amenity_ids' in kwargs and kwargs['amenity_ids']:
            self.amenity_ids = kwargs['amenity_ids']
