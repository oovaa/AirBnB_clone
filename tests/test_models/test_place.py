#!/usr/bin/python3
"""Unit test for Place class"""

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test to check for use of Place class"""

    def setUp(self):
        """Return to empty"""
        self.place_instance = Place()

    def test_module_doc(self):
        """check for module doc"""
        self.assertTrue(len(Place.__doc__) > 0)

    def test_class_doc(self):
        """check for class doc"""
        self.assertTrue(len(Place.__doc__) > 0)

    def test_name_initialization(self):
        """check if name is initalised"""
        self.assertEqual(self.place_instance.name, "")

    def test_field_types(self):
        """ Test field attributes of user """
        self.assertTrue(type(Place.city_id) is str)
        self.assertTrue(type(Place.user_id) is str)
        self.assertTrue(type(Place.name) is str)
        self.assertTrue(type(Place.description) is str)
        self.assertTrue(type(Place.number_rooms) is int)
        self.assertTrue(type(Place.number_bathrooms) is int)
        self.assertTrue(type(Place.max_guest) is int)
        self.assertTrue(type(Place.price_by_night) is int)
        self.assertTrue(type(Place.latitude) is float)
        self.assertTrue(type(Place.longitude) is float)
        self.assertTrue(type(Place.amenity_ids) is list)


if __name__ == '__main__':
    unittest.main()
