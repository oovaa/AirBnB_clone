#!/usr/bin/python3
"""CLI"""

import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
