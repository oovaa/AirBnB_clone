#!/usr/bin/python3
"""City Class"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class for AirBnB project.

    Attributes:
        state_id (str): The state ID associated with the city.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new City instance.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)

        state_id = kwargs.get('state_id', '')
        name = kwargs.get('name', '')

        # Set values only if they are not empty
        if state_id:
            self.state_id = state_id
        if name:
            self.name = name
