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

    def do_create(self, input_str):
        """Create instance of BaseModel & save json file"""
        args = input_str.split()

        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in HBNBCommand.actual_class:
            print("** class doesn't exist**")

        else:
            target_class = globals()[args[0]]
            new = target_class()
            print(new.id)
            new.save()

    def do_show(self, input_str):
        """Prints the string repre of instance based on class name & id"""
        args = input_str.split()

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

    def do_destroy(self, input_str):
        """Deletes an instance based on the class name and id"""
        args = input_str.split()

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

    def do_all(self, input_str):
        """Prints all str rep of all insts based or not on the class name."""
        args = input_str.split()

        if args[0] not in HBNBCommand.actual_class:
            print("** class doesn't exist **")
            return
        else:
            instances = []
            for key, obj in storage.all().items():
                if key.startswith(args[0]):
                    instances.append(str(obj))

        print(instances)

    def update_inst(self, input_str):
        """Updates an instance based on ID with dictionary from string"""
        # Validate the pattern
        pattern = r'^([a-zA-Z_]\w*)\.update\(([a-zA-Z_]\w*), (\{.*\})\)$'

        # Check if the string matches the pattern
        match = re.match(pattern, input_str.strip())
        if not match:
            print(
                "Invalid update format. Use: <class name>.update(<id>,\
                    <dictionary representation>)", input_str)

            return

        # Extract information using named groups
        class_name, inst_id, dict_repr = match.groups()

        class_obj = globals()[class_name]
        key = f"{class_obj.__name__}.{inst_id}"
        found = storage.all()

        if key in found:
            input_instance = found[key]

            # Convert the dictionary representation to a Python dictionary
            attr_dict = eval(dict_repr)

            if "id" in attr_dict \
                    or "created_at" in attr_dict or "updated_at" in attr_dict:
                print("Cannot update id, created_at, or updated_at")
                return

            for k, v in attr_dict.items():
                # Use getattr with a default value to handle non-existent ones
                current_value = getattr(input_instance, k, None)

                # Check if the attribute exists
                if current_value is not None:
                    setattr(input_instance, k, type(current_value)(v))
                else:
                    print(
                        "Attribute {} does not exist in {}".format(
                            k, class_obj.__name__
                        ))
            input_instance.save()
        else:
            print("** no instance found **")

    def do_update(self, input_str):
        """Updates inst based on class name & id by adding or updating attr"""
        args = input_str.split()

        regex = r'^[a-zA-Z_]\w*\.update\(\w+, \{.*\}\)$'
        if not re.match(regex, input_str.strip()):
            print("** Invalid update command format **", input_str)
            return

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

    def do_count(self, line):
        """Prints all str rep of all insts based or not on the class name."""
        args = line.split()

        if args[0] not in HBNBCommand.actual_class:
            print("** class doesn't exist **")
            return
        else:
            i = 0
            for key, _ in storage.all().items():
                if key.startswith(args[0]):
                    i += 1
            print(i)

    def precmd(self, line):
        actual_cmd = ""

        # Validate the pattern
        pattern = r'^([a-zA-Z_]\w*)\.([a-zA-Z_]\w*)\(([^)]*)\)$'

        # Check if the string matches the pattern
        match = re.match(pattern, line.strip())
        if not match:
            # Return the original command if not matching the pattern
            return line

        # Extract information using named groups
        class_part, method_part, method_args = match.groups()

        # Get the actual command
        actual_cmd = "{} {} {}".format(method_part, class_part, method_args)

        return actual_cmd.replace('"', '').replace(',', '')


if __name__ == '__main__':
    HBNBCommand().cmdloop()

    # def precmd(self, line):

    #     actual_cmd = ""
    #     line = line.strip()
    #     # validate the battren
    #     to_check = line
    #     pattern = r'^([a-zA-Z_]\w*)\.([a-zA-Z_]\w*)\(([^)]*)\)$'
    #     # Check if the string matches the pattern
    #     if not re.match(pattern, to_check):
    #         # return the command if not
    #         return line

    #     # split and store
    #     class_part = line.split(".")[0]
    #     method_part = line.split(".")[1]
    #     method_args = method_part[method_part.index("(")+1:-1]
    #     method_part = method_part[:method_part.index("(")]

    #     # get the actual command
    #     actual_cmd = "{} {} {}".format(method_part, class_part, method_args)

    #     return actual_cmd

    # <class name>.count()
    # <class name>.show(<id>)
    # <class name>.destroy(<id>)
    # <class name>.update(<id>, <attribute name>, <attribute value>)
    # <class name>.update(<id>, <dictionary representation>)

    # classes = {
    #     "User": User,
    #     "BaseModel": BaseModel,
    #     "City": City,
    #     "Place": Place,
    #     "Amenity": Amenity,
    #     "State": State,
    #     "Review": Review
    # }
    # actual_cmd = ""
    # cls_name = ""
    # method = ""
    # args = ""

    # # Check if the command matches the patterns
    # if re.match(r'^\w+\.(count|show|destroy|update)\(.+\)$', line):
    #     # Validate the class name
    #     cls_name, rest = line.split(".", 1)
    #     if cls_name not in classes:
    #         print("** class doesn't exist **")
    #         return ""

    #     # Split the method and arguments
    #     method, args = re.match(r'(\w+)\((.+)\)', rest).groups()
    #     args = args.strip()

    #     # Construct the valid command
    #     if method == "update":
    #         args = args.split(", ")
    #         args = ' '.join(args)
    #         actual_cmd = f"{method} {cls_name} {args}"
    #     else:
    #         actual_cmd = f"{cls_name} {method} {args}"
    # else:
    #     # If not, split the line and construct the command
    #     line_parts = line.split(".")
    #     cls_name = line_parts[0]
    #     if cls_name not in classes:
    #         print("** class doesn't exist **")
    #         return ""

    #     method = line_parts[1].split("(")[0]
    #     actual_cmd = f"{cls_name} {method}"
