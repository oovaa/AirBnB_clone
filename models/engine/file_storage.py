#!/usr/bin/python3


import json
import os
from models.base_model import BaseModel


class FileStorage:
    __file_path = os.path.join(os.getcwd(), 'file.json')
    __objects = dict()

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[obj.id] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w') as file:
            for k, v in FileStorage.__objects.items():
                json.dump(v.to_dict(), file)
                file.write('\n')  # Add a newline between objects
    def reload(self):
        try:
            if os.path.exists(FileStorage.__file_path) and os.path.getsize(FileStorage.__file_path) > 0:
                with open(FileStorage.__file_path) as f:
                    objdict = json.load(f)
                    obj_cls = objdict.get('__class__')
                    classes = {'BaseModel': BaseModel}

                    if obj_cls in classes:
                        cls = classes[obj_cls]
                        obj = cls()

                        for k, v in objdict.items():
                            if k != '__class__':
                                setattr(obj, k, v)

                        FileStorage.__objects[obj.id] = obj
                    else:
                        print(f"Warning: Class {obj_cls} not found.")
            else:
                print("Warning: File is empty or does not exist.")

        except FileNotFoundError:
            return
