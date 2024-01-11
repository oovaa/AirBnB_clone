#!/usr/bin/python3


import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serialized_objects = {key: obj.to_dict()
                              for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name = key.split('.')[0]

                    cls = globals()[class_name]
                    obj = cls(**obj_dict)
                    FileStorage.__objects[key] = obj
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass
