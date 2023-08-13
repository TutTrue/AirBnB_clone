#!/usr/bin/python3
"""Unittest for FileStorage model
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import models
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

import os
import unittest


class Test_FileStorage_model(unittest.TestCase):
    """
    test class for the FileStorage model.
    """

    def test_default_values(self):
        """
        test the default values for the FileStorage model
        os.remove("file.json")
        """
        storage = FileStorage()
        # self.assertEqual(storage._file_path, "file.json")
        # self.assertIsInstance(storage._file_path, str)
        # self.assertEqual(storage.all(), {})
        
        self.assertIsInstance(storage.all(), dict)
        # print(storage.reload())
        # print(storage.all()['Place.95c566ce-3d9b-4bfe-993c-29889bb29c65'])
        # self.assertEqual(storage.reload(), storage.all())
        
        
        base = BaseModel()
        base.save()
        objs = storage.all()
        obj =objs[f"{base.__class__.__name__}.{base.id}"]        
        self.assertEqual(base, obj)

        self.assertIsInstance(models.storage , FileStorage)
        """"
            test save class method
        """
        before_update_time = base.updated_at
        base.my_number = 90
        base.save()
        after_update_time = base.updated_at
        self.assertNotEqual(before_update_time, after_update_time)
        new_number = obj.my_number
        self.assertEqual(new_number, 90)




"""Unittest for base model
"""
import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    test class for the max_integer() function.
    """
    base = BaseModel()
    base.name = "My First Model"
    base.my_number = 89

    def test_create_instance_without_kwargs(self):
        """
        create an instance of class without kwargs
        """
        self.assertIsInstance(self.base, BaseModel)
        self.assertIsInstance(self.base.id, str)
        self.assertIsInstance(self.base.created_at, datetime)
        self.assertIsInstance(self.base.updated_at, datetime)
        self.assertEqual(self.base.name, "My First Model")
        self.assertEqual(self.base.my_number, 89)

    def test_create_instance_with_kwargs(self):
        """
        create an instance of class using kwargs
        """
        my_base_json = self.base.to_dict()
        new_base = BaseModel(**my_base_json)
        self.assertIsInstance(new_base, BaseModel)
        self.assertIsInstance(new_base.id, str)
        self.assertIsInstance(new_base.created_at, datetime)
        self.assertIsInstance(new_base.updated_at, datetime)
        self.assertEqual(new_base.name, "My First Model")
        self.assertEqual(new_base.my_number, 89)
        self.assertNotEqual(new_base, self.base)
        self.assertDictEqual(new_base.__dict__, self.base.__dict__)

    def test_to_dict(self):
        """
            test to_dict class method
        """
        to_dict_returned_dict = self.base.to_dict()
        expected_dic = self.base.__dict__.copy()
        expected_dic["__class__"] = self.base.__class__.__name__
        expected_dic["updated_at"] = self.base.updated_at.isoformat()
        expected_dic["created_at"] = self.base.created_at.isoformat()
        self.assertDictEqual(expected_dic, to_dict_returned_dict)

    def test_save(self):
        """"
            test save class method
        """
        before_update_time = self.base.updated_at
        self.base.my_number = 90
        self.base.save()
        after_update_time = self.base.updated_at
        self.assertNotEqual(before_update_time, after_update_time)
        all_objects = storage.all()
        obj = all_objects[f"{self.base.__class__.__name__}.{self.base.id}"]
        new_number = obj.my_number
        self.assertEqual(new_number, 90)

    def test_str(self):
        """
            test str method

            check for string representaion
        """
        expected_str = f"[{self.base.__class__.__name__}] ({self.base.id}) {self.base.__dict__}"
        self.assertEqual(self.base.__str__(), expected_str)
