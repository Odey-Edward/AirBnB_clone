#!/usr/bin/python3
"""Unittest for the BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test class for the BaseModel class"""

    b2 = BaseModel()
    b1 = BaseModel()

    def test_instance(self):
        """test case for BaseModel instances"""
        self.assertIsInstance(self.b1, BaseModel)

    def test_uniqueId(self):
        """test for unique id"""
        self.assertNotEqual(self.b2.id, self.b1.id)

    def test_datetime(self):
        """test for the created and updated time"""
        self.assertIsInstance(self.b1.created_at, datetime)
        self.assertIsInstance(self.b1.updated_at, datetime)
        self.assertNotEqual(self.b1.created_at, self.b2.created_at)
        self.assertNotEqual(self.b1.updated_at, self.b2.updated_at)
        
        outdated_time = self.b1.updated_at
        self.b1.save()

        self.assertNotEqual(outdated_time, self.b1.updated_at)

