#!/usr/bin/python3
"""Amenity Class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class for AirBnB project.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new Amenity instance.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')
