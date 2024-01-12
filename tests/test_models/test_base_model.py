#!/usr/bin/python3
"""Unit test for Base class"""

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestBase(unittest.TestCase):
    """Tests for Base Class"""

    def setUp(self):
        """setup"""
        self.model = BaseModel()

    def test_attr_exist(self):
        """assert that all required attributes exist in the base model"""
        assert hasattr(self.model, 'id')
        assert hasattr(self.model, 'updated_at')
        assert hasattr(self.model, 'created_at')

    def test_createdatType(self):
        """assert type of created at is datetime"""
        assert isinstance(self.model.created_at, datetime)

    def test_updatedType(self):
        """assert type of updated at is datetime"""
        assert isinstance(self.model.updated_at, datetime)

    def test_todict(self):
        """Ensure to_dict method of BM class
        created a dict repr with expe keys"""
        dict_repr = self.model.to_dict()
        self.assertIsInstance(dict_repr, dict)
        self.assertIn('__class__', dict_repr)
        self.assertEqual(dict_repr['__class__'], 'BaseModel')
        self.assertIn('id', dict_repr)
        self.assertIn('created_at', dict_repr)
        self.assertIn('updated_at', dict_repr)

    def test_str(self):
        """Ensure str method of BM class makes a str repr of attr"""
        str_repr = str(self.model)
        self.assertIn('BaseModel', str_repr)
        self.assertIn('id', str_repr)
        self.assertIn('created_at', str_repr)
        self.assertIn('updated_at', str_repr)

    def tearDown(self) -> None:
        """Reset FileStorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)


if __name__ == '__main__':
    unittest.main()
