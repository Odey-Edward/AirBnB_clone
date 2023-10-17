#!/usr/bin/python3

import os
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test class for the FileStorage Class"""

    def test_file_path(self):
        """test case for the file path"""

        with self.assertRaises(AttributeError):
            FileStorage.file_path

        with self.assertRaises(AttributeError):
            FileStorage.__file_path

        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))

        file_path = FileStorage._FileStorage__file_path

        self.assertIsInstance(file_path, str)

        if os.path.exists(file_path):
            os.remove(file_path)

        base = BaseModel()
        self.assertFalse(os.path.exists(file_path))

        base.save()
        self.assertTrue(os.path.exists(file_path))
        os.remove(file_path)

    def test_objects(self):
        """test case for FileStorage object attribute"""

        with self.assertRaises(AttributeError):
            FileStorage.objects

        with self.assertRaises(AttributeError):
            FileStorage.__objects

        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))

        objects = FileStorage._FileStorage__objects

        self.assertIsInstance(objects, dict)
