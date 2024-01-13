#!/usr/bin/python3
"""base modle"""

from datetime import datetime
import uuid
import models


class BaseModel:
    """The BaseModel class is the base class for all
        models in the AirBnB clone project.

    Attributes:
        id (str): The unique identifier for each instance.
        created_at (datetime): The datetime when the instance is created.
        updated_at (datetime): The datetime when the instance is last updated.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    if key != '__class__':
                        setattr(self, key, value)
            models.storage.new(self)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel instance.

        Returns:
            dict: A dictionary containing all attributes of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__

        if 'created_at' in obj_dict:
            if not isinstance(obj_dict['created_at'], datetime):
                obj_dict['created_at'] = datetime.fromisoformat(
                    obj_dict['created_at'])

            obj_dict['created_at'] = obj_dict['created_at'].isoformat()

        if 'updated_at' in obj_dict:
            if not isinstance(obj_dict['updated_at'], datetime):
                obj_dict['updated_at'] = datetime.fromisoformat(
                    obj_dict['updated_at'])
            obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()

        return obj_dict

    def __str__(self):
        """Returns a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
