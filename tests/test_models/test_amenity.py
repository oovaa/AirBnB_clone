#!/usr/bin/python3
"""Unit test for Amenity class"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test to check for use of Amenity class"""

    def setUp(self):
        """Return to empty"""
        self.amenity_instance = Amenity()

    def test_module_doc(self):
        """check for module doc"""
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_class_doc(self):
        """check for class doc"""
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_name_initialization(self):
        self.assertEqual(self.amenity_instance.name, "")


if __name__ == '__main__':
    unittest.main()
