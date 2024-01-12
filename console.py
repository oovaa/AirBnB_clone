#!/usr/bin/python3
"""CLI"""

import cmd
from json import loads
import re
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Entry point to CI"""

    prompt = "(hbnb) "
    actual_class = ["BaseModel", "User", "Place",
                    "State", "City", "Amenity", "Review"]

    def do_quit(self, *args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, *args):
        """Exit program"""
        return True

    def emptyline(self):
        """Execute nothing"""
        pass

    def do_create(self, input):
        """Create instance of BaseModel & save json file"""
        args = input.split()

        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in HBNBCommand.actual_class:
            print("** class doesn't exist**")

        else:
            target_class = globals()[args[0]]
            new = target_class()
            print(new.id)
            new.save()

    def do_show(self, input):
        """Prints the string repre of instance based on class name & id"""
        args = input.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.actual_class:
            print("** class doesn't exist **")
        elif len(args) <= 1:
            print("** instance id missing **")
        else:
            target_class = globals()[args[0]]
            inst_id = args[1]
            if target_class:
                key = f"{args[0]}.{inst_id}"
                obj = storage.all()
                if key in obj:
                    print(obj[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, input):
        """Deletes an instance based on the class name and id"""
        args = input.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.actual_class:
            print("** class doesn't exist **")
        elif len(args) <= 1:
            print("** instance id missing **")
        else:
            target_class = globals()[args[0]]
            inst_id = args[1]
            key = f"{args[0]}.{inst_id}"
            obj = storage.all()
            if key in obj:
                del obj[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, input):
        """Prints all str rep of all insts based or not on the class name."""
        args = input.split()

        if args[0] not in HBNBCommand.actual_class:
            print("** class doesn't exist **")
            return
        else:
            instances = []
            for key, obj in storage.all().items():
                if key.startswith(args[0]):
                    instances.append(str(obj))

        print(instances)

    def do_update(self, input):
        """Updates inst based on class name & id by adding or updating attr"""
        args = input.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.actual_class:
            print("** class doesn't exist **")
            return
        elif len(args) <= 1:
            print("** instance id missing **")
            return
        elif all(key.split('.')[1] != args[1] for key in storage.all().keys()):
            print("** no instance found **")
            return
        elif len(args) <= 2:
            print("** attribute name missing **")
            return
        elif len(args) <= 3:
            print("** value missing **")
            return

        target_class = globals()[args[0]]
        inst_id = args[1]
        attr_name = args[2]
        attr_val = args[3].strip('"')

        key = f"{args[0]}.{inst_id}"
        obj = storage.all()

        if key in obj:
            instance = obj[key]

            # Ensure id, created_at, and updated_at are not updated
            if attr_name in ["id", "created_at", "updated_at"]:
                print(f"Cannot update {attr_name}")
                return

            # If the attribute doesn't exist, add it to the instance
            if not hasattr(instance, attr_name):
                setattr(instance, attr_name, "")

            # Update the attribute value on the instance
            setattr(instance, attr_name, type(
                getattr(instance, attr_name))(attr_val))
            instance.save()
        else:
            print("** no instance found **")
            return

    def precmd(self, line):
        classes = {
            "User": User,
            "BaseModel": BaseModel,
            "City": City,
            "Place": Place,
            "Amenity": Amenity,
            "State": State,
            "Review": Review
        }
        methods = {
            "all": HBNBCommand.do_all
        }
        actual_cmd = ""

        line = line.split(".")

        cls_name = line[0]
        method = line[1][0: -2]

        actual_cmd = "{} {}".format(cls_name, method)

        print(actual_cmd)

        return actual_cmd


if __name__ == '__main__':
    HBNBCommand().cmdloop()
    
    <class name>.count().
    <class name>.show(<id>).
    <class name>.destroy(<id>).
    <class name>.update(<id>, <attribute name>, <attribute value>).
<class name>.update(<id>, <dictionary representation>).

