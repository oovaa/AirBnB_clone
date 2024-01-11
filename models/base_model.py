#!/usr/bin/python3
"""base modle"""

from datetime import datetime
import uuid
import models


class BaseModel:

    def __init__(self, *args, **kwargs):
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
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):

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
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
