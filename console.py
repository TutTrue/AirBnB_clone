#!/usr/bin/env python3
"""
 the entry point of the command interpreter
"""


import cmd
from models.engine import file_storage
from models import storage
from models import FileStorage
from models.user import User
from models.user import BaseModel
import json
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

        obj = eval(args[0])() # eval creates an instance
        obj.save()
        print(obj.id)

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
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        objs = FileStorage().all()
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
        if f"{args[0]}.{args[1]}" not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        
            # cast the value to the right type
        if args[3].isdigit():
            a_value = int(args[3])
        else:
            try:
                a_value = float(args[3])
            except ValueError:
                a_value = args[3].replace('"' , "")
        for key, obj in objs.items():
            if f"{args[0]}.{args[1]}" == key:
                setattr(obj, args[2], a_value)
                storage.save()
                return

        
    def onecmd(self, line):
        if '.' in line:
            objs = FileStorage().all()
            cls, mthd = line.split('.')
            if mthd == "all()":
                print ("[" ,end ="")
                for obj in objs.values():
                    if obj.__class__.__name__ == cls:                        
                        print(obj, end ="")     
                print("]")
                
            elif mthd == "count()":
                all = []
                for obj in objs.values():
                    if obj.__class__.__name__ == cls:
                        all.append(obj)
                print(len(all))
            
            elif mthd[0:4] =="show":
                self.do_show(f"{cls} {mthd[6:-2]}")
                
            elif mthd[0:7] == "destroy":
                self.do_destroy(f"{cls} {mthd[9:-2]}")

            elif mthd[0:6] == "update":
                id,attr =mthd[7:-1].split(",", 1)
                id=id.split('"')[1]
                try:
                    att =json.loads(attr.replace("'" , '"'))
                    print(att)
                    for k,v in att.items():
                            print(f"{cls} {id} {k} {v}")
                            self.do_update(f"{cls} {id} {k} {v}")
                except Exception as e:
                    attr,val = attr.split(',')
                    attr =attr.split('"')[1]
                    self.do_update(f"{cls} {id} {attr} {val}")
                    
                

if __name__ == '__main__':
    HBNBCommand().cmdloop()
