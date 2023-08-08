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

    def do_create(self, args):
        """Creates a new instance of a class"""
        args = args.split()
        if not args[0]:
            print("** class name missing **")
            return
        try:
            obj = eval(args[0])
            obj.save()
            print(obj.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        Prints the string representation of an
        instance based on the class name and id.
        """
        pass

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        """
        pass

    def do_all(self, args):
        """
         Prints all string representation of all 
         instances based or not on the class name.
        """
        pass

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
