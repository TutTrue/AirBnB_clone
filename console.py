#!/usr/bin/env python3
"""
 the entry point of the command interpreter
"""


import cmd
class HBNBCommand(cmd.Cmd):
    """My console class"""

    prompt = "(hbnb) "
    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing when empty line or Enter key"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
