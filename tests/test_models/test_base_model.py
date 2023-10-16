#!/usr/bin/python3
"""Unittest for the BaseModel class"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test class for the BaseModel class"""

    b2 = BaseModel()

    def test_instance(self):
        """test case for BaseModel instances"""
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)
