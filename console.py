#!/usr/bin/python3
"""CLI"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Entry point to CI"""

    prompt = "(hbnb)"

    def do_quit(self, *args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, *args):
        """Exit program"""
        return True

    def emptyline(self):
        """Execute nothing"""
        pass

    def do_create(self, line):
        """Create instance of BaseModel & save json file"""
        args = line.split()
        actual_class = ["BaseModel"]

        if len(args) <= 0:
            print("** class name missing **")

        elif args[0] not in actual_class:
            print("** class doesn't exist**")

        else:
            target_class = globals()[args[0]]
            new = target_class()
            print(new.id)
            new.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
