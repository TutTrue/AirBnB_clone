#!/usr/bin/env python3
"""Unittest for the console
"""
import unittest
from console import HBNBCommand
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
from models import storage
import os


class Test_Console(unittest.TestCase):
    """
    test class for the console.
    """

    def test_prompt(self):
        """test the prompt"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertEqual(HBNBCommand().prompt, "(hbnb) ")

    def test_help_messages(self):
        """
        test help messages for the commands
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(
                "\n        Quit command to exit the program\n" +
                "        Usage: quit\n        \n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(
                "\n        Quit command to exit the program\n" +
                "        Usage: ctrl + d\n        \n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(
                "\n        Creates a new instance of a class\n" +
                "        Usage: create <Class Name>\n        \n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual(
                "\n        Prints the string representation" +
                " of an\n        instance based on the class name and id.\n" +
                "        Usage: show <Class Name> <ID>\n        \n",
                f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(
                "\n        Deletes an instance based on the class name " +
                "and id\n        Usage: destroy <Class Name> <ID>\n        \n",
                f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertEqual(
                "\n        Prints all string representation of all\n" +
                "        instances based or not on the class name.\n" +
                "        Usage: all\n" +
                "        Usage: all <Class Name>\n        \n",
                f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertEqual(
                "\n        Updates an instance based on the class name" +
                " and id\n        by adding or updating attribute" +
                " (save the change into the JSON file)\n        " +
                "Usage: update <class name> <id> <attribute name>" +
                " \"<attribute value>\"\n        \n",
                f.getvalue())
