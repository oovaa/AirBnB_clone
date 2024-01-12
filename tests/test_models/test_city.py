#!/usr/bin/python3
"""Unit test for City class"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test to check for use of City class"""

    def setUp(self):
        """Return to empty"""
        self.city_instance = City()

    def test_module_doc(self):
        """check for module doc"""
        self.assertTrue(len(City.__doc__) > 0)

    def test_class_doc(self):
        """check for class doc"""
        self.assertTrue(len(City.__doc__) > 0)

    def test_name_initialization(self):
        """check if name is initialized"""
        self.assertEqual(self.city_instance.name, "")


if __name__ == '__main__':
    unittest.main()
