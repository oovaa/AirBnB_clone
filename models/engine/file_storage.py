#!/usr/bin/python3


import json
import os


class FileStorage:
    __file_path = 'file.json'
    __objects = dict()

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[obj.id] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w') as file:
            for k, v in FileStorage.__objects.items():
                file.write(json.dumps(v.to_dict()))
                file.write('\n')  # Add a newline between objects

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                for line in file:
                    obj_dict = json.loads(line)
                    class_name = obj_dict.pop('__class__', None)
                    if class_name:
                        cls = eval(class_name)
                        obj = cls(**obj_dict)
                        FileStorage.__objects[obj.id] = obj
