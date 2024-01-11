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
        self.assertEqual(self.place_instance.name, "")

    def test_field_types(self):
        """ Test field attributes of user """
        self.assertTrue(type(Place.city_id) == str)
        self.assertTrue(type(Place.user_id) == str)
        self.assertTrue(type(Place.name) == str)
        self.assertTrue(type(Place.description) == str)
        self.assertTrue(type(Place.number_rooms) == int)
        self.assertTrue(type(Place.number_bathrooms) == int)
        self.assertTrue(type(Place.max_guest) == int)
        self.assertTrue(type(Place.price_by_night) == int)
        self.assertTrue(type(Place.latitude) == float)
        self.assertTrue(type(Place.longitude) == float)
        self.assertTrue(type(Place.amenity_ids) == list)


if __name__ == '__main__':
    unittest.main()
