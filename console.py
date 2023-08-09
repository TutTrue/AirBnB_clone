#!/usr/bin/env python3
"""
 the entry point of the command interpreter
"""


import cmd
from models.engine import file_storage
from models import FileStorage
from models.user import User
from models.user import BaseModel

class HBNBCommand(cmd.Cmd):
    """My console class"""

    prompt = "(hbnb) "
    __models = {"BaseModel", "User", "State", "City", "Place", "Amenity",
        "Review"}
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
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] not in self.__models:
            print("** class doesn't exist **")
            return

        obj = eval(args[0])()
        print(obj.id)
        obj.save()

    def do_show(self, args):
        """
        Prints the string representation of an
        instance based on the class name and id.
        """
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] not in self.__models:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if f"{args[0]}.{args[1]}" not in FileStorage().all():
            print("** no instance found **")
            return
        print(FileStorage().all()[f"{args[0]}.{args[1]}"])

            
    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        """
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] not in self.__models:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if f"{args[0]}.{args[1]}" not in FileStorage().all():
            print("** no instance found **")
            return
        
        del FileStorage().all()[f"{args[0]}.{args[1]}"]
        
        FileStorage().save()
        

    def do_all(self, args):
        """
         Prints all string representation of all 
         instances based or not on the class name.
        """
        objs = FileStorage().all()
        if not args:
            print([str(obj) for obj in objs.values()])
            return
        args = args.split()
        if args[0] not in self.__models:
            print("** class doesn't exist **")
            return
        li = []
        for obj in objs.values():
            if obj.__class__.__name__ == args[0]:
                li.append(str(obj))
        print(li)



    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
