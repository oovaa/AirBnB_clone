#!/usr/bin/python3
"""State Class"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class for AirBnB project.

    Attributes:
        name (str): The name of the state.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new State instance.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)

        if 'name' in kwargs and kwargs['name']:
            self.name = kwargs['name']
