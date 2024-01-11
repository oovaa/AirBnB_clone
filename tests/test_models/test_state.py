#!/usr/bin/python3
"""Unit test for State class"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test to check for use of State class"""

    def setUp(self):
        """Return to empty"""
        self.state_instance = State()

    def test_module_doc(self):
        """check for module doc"""
        self.assertTrue(len(State.__doc__) > 0)

    def test_class_doc(self):
        """check for class doc"""
        self.assertTrue(len(State.__doc__) > 0)

    def test_name_initialization(self):
        self.assertEqual(self.state_instance.name, "")


if __name__ == '__main__':
    unittest.main()
