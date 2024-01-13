#!/usr/bin/python3
"""User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class for AirBnB project.

    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new User instance.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)

        if 'email' in kwargs and kwargs['email']:
            self.email = kwargs['email']
        if 'password' in kwargs and kwargs['password']:
            self.password = kwargs['password']
        if 'first_name' in kwargs and kwargs['first_name']:
            self.first_name = kwargs['first_name']
        if 'last_name' in kwargs and kwargs['last_name']:
            self.last_name = kwargs['last_name']
