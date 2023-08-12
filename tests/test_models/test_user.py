#!/usr/bin/python3
"""Unittest for base model
"""
import unittest
from models.user import User
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestConstructor(unittest.TestCase):
    """
    test class for the max_integer() function.
    """

    def test_create_instance_without_kwargs(self):
        """
        create an instance of class without kwargs
        """
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
