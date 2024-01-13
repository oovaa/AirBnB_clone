#!/usr/bin/python3
"""Unit test for Review class"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test to check for use of Review class"""

    def setUp(self):
        """Return to empty"""
        self.review_instance = Review()

    def test_module_doc(self):
        """check for module doc"""
        self.assertTrue(len(Review.__doc__) > 0)

    def test_class_doc(self):
        """check for class doc"""
        self.assertTrue(len(Review.__doc__) > 0)

    def test_text_initialization(self):
        """check if text is initailzed"""
        self.assertEqual(self.review_instance.text, "")

    def test_field_types(self):
        """ Test field attributes of user """
        my_Review = Review()
        self.assertTrue(type(my_Review.place_id) is str)
        self.assertTrue(type(my_Review.user_id) is str)
        self.assertTrue(type(my_Review.text) is str)


if __name__ == '__main__':
    unittest.main()
