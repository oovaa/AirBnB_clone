#!/usr/bin/python3
"""Review Class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class for AirBnB project.

    Attributes:
        place_id (str): The place ID associated with the review.
        user_id (str): The user ID associated with the review.
        text (str): The text content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new Review instance.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)

        if 'place_id' in kwargs and kwargs['place_id']:
            self.place_id = kwargs['place_id']
        if 'user_id' in kwargs and kwargs['user_id']:
            self.user_id = kwargs['user_id']
        if 'text' in kwargs and kwargs['text']:
            self.text = kwargs['text']
