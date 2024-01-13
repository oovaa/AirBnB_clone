#!/usr/bin/python3

"""file storage """

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:

    """This class manages the serialization and deserialization of objects to a
    JSON file.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary containing objects
        stored with their keys.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the dictionary.

        Args:
            obj: The object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves the serialized objects to the JSON file."""
        serialized_objects = {key: obj.to_dict()
                              for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Reloads objects from the JSON file to the dictionary."""
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
