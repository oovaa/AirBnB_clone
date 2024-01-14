#!/usr/bin/python3

from models.engine.file_storage import FileStorage
from io import StringIO
import json
import unittest
from unittest.mock import patch
from console import HBNBCommand as cons
from models.base_model import BaseModel
import models


class TestCommands(unittest.TestCase):

    def setUp(self):
        self.base_model_instance = BaseModel()
        self.base_model_instance.save()

    def tearDown(self):
        pass  # If you need to perform any cleanup after the tests

    def assertCommandOutput(self, command):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            cons().onecmd(command)
            return mock_stdout.getvalue().strip()

    def test_create(self):
        # Use the ID of the created instance in setUp

        # Test cases for missing class name
        self.assertEqual(self.assertCommandOutput(
            "create"), "** class name missing **")
        # Test cases for non-existing class
        self.assertEqual(self.assertCommandOutput(
            "create MyModel"), "** class doesn't exist **")

    def test_show(self):
        # Use the ID of the created instance in setUp
        expected_output = str(self.base_model_instance)
        self.assertEqual(self.assertCommandOutput(
            f"show BaseModel {self.base_model_instance.id}"), expected_output)

        # Test cases for missing class name
        self.assertEqual(self.assertCommandOutput(
            "show"), "** class name missing **")
        # Test cases for non-existing class
        self.assertEqual(self.assertCommandOutput(
            "show MyModel"), "** class doesn't exist **")
        # Test cases for missing instance id
        self.assertEqual(self.assertCommandOutput(
            "show BaseModel"), "** instance id missing **")
        # Test cases for non-existing instance
        self.assertEqual(self.assertCommandOutput(
            "show BaseModel 121212"), "** no instance found **")

    # Similar test methods for other commands (destroy, all, update)...


    def test_all(self):
        # Use the ID of the created instance in setUp
        # Convert the instance to a string
        expected_output = str(list(models.storage.all().values())[0])  # Convert the instance to a string
        actual_output = self.assertCommandOutput("all BaseModel")

        # print("Expected Output:", expected_output)    TODO
        # print("Actual Output  :", actual_output)

        # self.assertListEqual([actual_output], [f"[{expected_output}]"])

        # Test cases for non-existing class
        self.assertEqual(self.assertCommandOutput(
            "all MyModel"), "** class doesn't exist **")

    def test_update(self):
        # Use the ID of the created instance in setUp
        expected_output = ""
        self.assertEqual(self.assertCommandOutput(
            f"update BaseModel {self.base_model_instance.id} email 'aibnb@mail.com'"), expected_output)

        # Test cases for missing class name
        self.assertEqual(self.assertCommandOutput(
            "update"), "** class name missing **")
        # Test cases for non-existing class
        self.assertEqual(self.assertCommandOutput(
            "update MyModel"), "** class doesn't exist **")
        # Test cases for missing instance id
        self.assertEqual(self.assertCommandOutput(
            "update BaseModel"), "** instance id missing **")
        # Test cases for non-existing instance
        self.assertEqual(self.assertCommandOutput(
            "update BaseModel 121212"), "** no instance found **")
        # Test cases for missing attribute name
        self.assertEqual(self.assertCommandOutput(
            f"update BaseModel {self.base_model_instance.id}"), "** attribute name missing **")
        # Test cases for missing attribute value
        self.assertEqual(self.assertCommandOutput(
            f"update BaseModel {self.base_model_instance.id} first_name"), "** value missing **")


if __name__ == '__main__':
    unittest.main()
