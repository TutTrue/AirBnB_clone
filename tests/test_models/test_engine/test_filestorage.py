#!/usr/bin/python3
"""Unittest for FileStorage model
"""
import unittest
from models.engine.file_storage import FileStorage


class Test_FileStorage_model(unittest.TestCase):
    """
    test class for the FileStorage model.
    """

    def test_default_values(self):
        """
        test the default values for the FileStorage model
        """
        storage = FileStorage()
        # self.assertEqual(storage._file_path, "file.json")
        # self.assertIsInstance(storage._file_path, str)
        self.assertEqual(storage.all(), {})
        self.assertIsInstance(storage.all(), dict)
