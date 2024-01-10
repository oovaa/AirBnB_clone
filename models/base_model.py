#!/usr/bin/python3
"""base modle"""

from datetime import datetime
import json
import uuid
import models


class BaseModel:

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for k, v in kwargs.items():
                if k in ('__class__'):
                    continue
                if k in ('created_at', 'updated_at'):
                    try:
                        setattr(self, k, datetime.fromisoformat(v))
                    except ValueError:
                        print("Error converting {} to datetime: {}".format(k, v))
                else:
                    setattr(self, k, v)
        if not kwargs:
            models.storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()  # added

    def to_dict(self):

        obj_dict = self.__dict__
        obj_dict['__class__'] = self.__class__.__name__

        if 'created_at' in obj_dict:
            obj_dict['created_at'] = obj_dict['created_at'].isoformat()

        if 'updated_at' in obj_dict:
            obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()

        return obj_dict

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
