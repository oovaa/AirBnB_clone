#!/usr/bin/python3
"""Tests for AirBnB clone console"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models import storage


# Test HBNB
class TestHBNBCommand(unittest.TestCase):
    """Unit tests for HBNB command class"""

    def setUp(self):
        self.hbnb_command = HBNBCommand()

    def getCommandOutput(self, command):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(command)
            return mock_stdout.getvalue().strip()

    def test_help(self):
        h = ("Documented commands (type help <topic>):\n"
             "========================================\n"
             "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(h, output.getvalue().strip())

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            result = self.hbnb_command.onecmd("quit")
            self.assertTrue(result)  # Should return True to indicate quitting

    def test_EOF(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            result = self.hbnb_command.onecmd("EOF")
            self.assertTrue(result)  # Should return True to indicate quitting

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("create BaseModel")
            # Check if the output is a valid UUID
            self.assertTrue(len(output) == 36)

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd("create BaseModel")
            instance_id = mock_stdout.getvalue().strip()
            output = self.getCommandOutput(f"show BaseModel {instance_id}")
            # Check if the instance details are in the output
            self.assertTrue(instance_id in output)

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd("create BaseModel")
            instance_id = mock_stdout.getvalue().strip()
            self.hbnb_command.onecmd(f"destroy BaseModel {instance_id}")
            output = self.getCommandOutput(f"show BaseModel {instance_id}")
            # Check if the instance is deleted
            self.assertTrue("** no instance found **" in output)


# Test HBNB errors
class TestHBNBCommand_errors(unittest.TestCase):

    def setUp(self):
        self.hbnb_command = HBNBCommand()

    def getCommandOutput(self, command):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(command)
            return mock_stdout.getvalue().strip()

    def test_create_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("create")
            self.assertEqual(output, "** class name missing **")

    def test_create_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("create MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show")
            self.assertEqual(output, "** class name missing **")

    def test_show_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_id_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show BaseModel")
            self.assertEqual(output, "** instance id missing **")

    def test_show_id_not_found(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show BaseModel 213415ms")
            self.assertEqual(output, "** no instance found **")

    def test_destroy_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy")
            self.assertEqual(output, "** class name missing **")

    def test_destroy_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_instance_id_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy BaseModel")
            self.assertEqual(output, "** instance id missing **")

    def test_destroy_no_instance_found(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy BaseModel 121212")
            self.assertEqual(output, "** no instance found **")

    def test_all_with_class_name(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("all BaseModel")
            # You may want to assert the format of the output if it's specific
            self.assertNotEqual(output, "** class doesn't exist **")

    def test_all_nonexistent_class(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("all MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update")
            self.assertEqual(output, "** class name missing **")

    def test_update_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_instance_id_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update BaseModel")
            self.assertEqual(output, "** instance id missing **")

    def test_update_no_instance_found(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update BaseModel 121212")
            self.assertEqual(output, "** no instance found **")

    def test_update_attribute_name_missing(self):
        to_update = BaseModel()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput(f"update BaseModel {to_update.id}")
            self.assertEqual(output, "** attribute name missing **")

    def test_update_value_missing(self):
        to_update = BaseModel()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput(
                f"update BaseModel {to_update.id} first_name")
            self.assertEqual(output, "** value missing **")


# Test User
class TestConsoleWithUser(unittest.TestCase):
    def setUp(self):
        self.hbnb_command = HBNBCommand()

    def getCommandOutput(self, command):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(command)
            return mock_stdout.getvalue().strip()

    def test_create_user(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("create User")
            self.assertTrue(output is not None and len(output) > 0)

    def test_show_user(self):
        user_instance = User()
        user_id = user_instance.id
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput(f"show User {user_id}")
            expected_str = str(user_instance)
            self.assertEqual(expected_str, output)

    def test_destroy_user(self):
        user_instance = User()
        user_id = user_instance.id
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(f"destroy User {user_id}")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 0)

    def test_all_user(self):
        user_instance = User()
        user_id = user_instance.id
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(f"all User")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(str(user_instance) in output)

    def test_update_user(self):
        user_instance = User()
        user_id = user_instance.id
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(
                f"update User {user_id} email 'test@example.com'")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 0)

# Test User Errors


class Test_User_errors(unittest.TestCase):

    def setUp(self):
        self.hbnb_command = HBNBCommand()

    def getCommandOutput(self, command):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(command)
            return mock_stdout.getvalue().strip()

    def test_create_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("create")
            self.assertEqual(output, "** class name missing **")

    def test_create_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("create MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show")
            self.assertEqual(output, "** class name missing **")

    def test_show_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_id_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show User")
            self.assertEqual(output, "** instance id missing **")

    def test_show_id_not_found(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show User 213415ms")
            self.assertEqual(output, "** no instance found **")

    def test_destroy_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy")
            self.assertEqual(output, "** class name missing **")

    def test_destroy_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_instance_id_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy User")
            self.assertEqual(output, "** instance id missing **")

    def test_destroy_no_instance_found(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy User 121212")
            self.assertEqual(output, "** no instance found **")

    def test_all_with_class_name(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("all User")
            # You may want to assert the format of the output if it's specific
            self.assertNotEqual(output, "** class doesn't exist **")

    def test_all_nonexistent_class(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("all MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update")
            self.assertEqual(output, "** class name missing **")

    def test_update_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_instance_id_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update User")
            self.assertEqual(output, "** instance id missing **")

    def test_update_no_instance_found(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update User 121212")
            self.assertEqual(output, "** no instance found **")

    def test_update_attribute_name_missing(self):
        to_update = User()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput(f"update User {to_update.id}")
            self.assertEqual(output, "** attribute name missing **")

    def test_update_value_missing(self):
        to_update = User()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput(
                f"update User {to_update.id} first_name")
            self.assertEqual(output, "** value missing **")


# Test State
class TestConsoleWithState(unittest.TestCase):
    def setUp(self):
        self.hbnb_command = HBNBCommand()

    def getCommandOutput(self, command):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(command)
            return mock_stdout.getvalue().strip()

    def test_create_state(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("create State")
            self.assertTrue(output is not None and len(output) > 0)

    def test_show_state(self):
        state_instance = State()
        state_id = state_instance.id
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput(f"show State {state_id}")
            expected_str = str(state_instance)
            self.assertEqual(expected_str, output)

    def test_destroy_state(self):
        state_instance = State()
        state_id = state_instance.id
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(f"destroy State {state_id}")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 0)

    def test_all_state(self):
        state_instance = State()
        state_id = state_instance.id
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(f"all State")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(str(state_instance) in output)

    def test_update_state(self):
        state_instance = State()
        state_id = state_instance.id
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(
                f"update State {state_id} name 'New York'")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 0)

# Test State Errors


class Test_State_errors(unittest.TestCase):

    def setUp(self):
        self.hbnb_command = HBNBCommand()

    def getCommandOutput(self, command):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(command)
            return mock_stdout.getvalue().strip()

    def test_create_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("create")
            self.assertEqual(output, "** class name missing **")

    def test_create_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("create MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show")
            self.assertEqual(output, "** class name missing **")

    def test_show_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_id_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show State")
            self.assertEqual(output, "** instance id missing **")

    def test_show_id_not_found(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show State Berlin")
            self.assertEqual(output, "** no instance found **")

    def test_destroy_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy")
            self.assertEqual(output, "** class name missing **")

    def test_destroy_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_instance_id_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy State")
            self.assertEqual(output, "** instance id missing **")

    def test_destroy_no_instance_found(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy State Berlin")
            self.assertEqual(output, "** no instance found **")

    def test_all_with_class_name(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("all State")
            self.assertNotEqual(output, "** class doesn't exist **")

    def test_all_nonexistent_class(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("all MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update")
            self.assertEqual(output, "** class name missing **")

    def test_update_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_instance_id_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update State")
            self.assertEqual(output, "** instance id missing **")

    def test_update_no_instance_found(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update State Berlin")
            self.assertEqual(output, "** no instance found **")

    def test_update_attribute_name_missing(self):
        to_update = State()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput(f"update State {to_update.id}")
            self.assertEqual(output, "** attribute name missing **")

    def test_update_value_missing(self):
        to_update = State()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput(
                f"update State {to_update.id} name")
            self.assertEqual(output, "** value missing **")


# Test Review
class TestConsoleWithReview(unittest.TestCase):
    def setUp(self):
        self.hbnb_command = HBNBCommand()

    def getCommandOutput(self, command):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(command)
            return mock_stdout.getvalue().strip()

    def test_create_review(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("create Review")
            self.assertTrue(output is not None and len(output) > 0)

    def test_show_review(self):
        review_instance = Review()
        review_id = review_instance.id
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput(f"show Review {review_id}")
            expected_str = str(review_instance)
            self.assertEqual(expected_str, output)

    def test_destroy_review(self):
        review_instance = Review()
        review_id = review_instance.id
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(f"destroy Review {review_id}")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 0)

    def test_all_review(self):
        review_instance = Review()
        review_id = review_instance.id
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(f"all Review")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(str(review_instance) in output)

# Test Review Errors


class Test_Review_errors(unittest.TestCase):
    def setUp(self):
        self.hbnb_command = HBNBCommand()

    def getCommandOutput(self, command):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(command)
            return mock_stdout.getvalue().strip()

    def test_create_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("create")
            self.assertEqual(output, "** class name missing **")

    def test_create_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("create MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show")
            self.assertEqual(output, "** class name missing **")

    def test_show_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_id_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show Review")
            self.assertEqual(output, "** instance id missing **")

    def test_show_id_not_found(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show Review Berlin")
            self.assertEqual(output, "** no instance found **")

    def test_destroy_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy")
            self.assertEqual(output, "** class name missing **")

    def test_destroy_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_instance_id_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy Review")
            self.assertEqual(output, "** instance id missing **")

    def test_destroy_no_instance_found(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy Review Berlin")
            self.assertEqual(output, "** no instance found **")

    def test_all_with_class_name(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("all Review")
            self.assertNotEqual(output, "** class doesn't exist **")

    def test_all_nonexistent_class(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("all MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update")
            self.assertEqual(output, "** class name missing **")

    def test_update_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_instance_id_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update Review")
            self.assertEqual(output, "** instance id missing **")

    def test_update_no_instance_found(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update Review Berlin")
            self.assertEqual(output, "** no instance found **")

    def test_update_attribute_name_missing(self):
        to_update = Review()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput(f"update Review {to_update.id}")
            self.assertEqual(output, "** attribute name missing **")

    def test_update_value_missing(self):
        to_update = Review()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput(
                f"update Review {to_update.id} name")
            self.assertEqual(output, "** value missing **")


# Test Place
class TestConsoleWithPlace(unittest.TestCase):
    def setUp(self):
        self.hbnb_command = HBNBCommand()

    def getCommandOutput(self, command):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(command)
            return mock_stdout.getvalue().strip()

    def test_create_place(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("create Place")
            self.assertTrue(output is not None and len(output) > 0)

    def test_show_place(self):
        place_instance = Place()
        place_id = place_instance.id
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput(f"show Place {place_id}")
            expected_str = str(place_instance)
            self.assertEqual(expected_str, output)

    def test_destroy_place(self):
        place_instance = Place()
        place_id = place_instance.id
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(f"destroy Place {place_id}")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 0)

    def test_all_place(self):
        place_instance = Place()
        place_id = place_instance.id
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(f"all Place")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(str(place_instance) in output)

    def test_update_place(self):
        place_instance = Place()
        place_id = place_instance.id
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(
                f"update Place {place_id} 'New York'")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 0)

# Test Place Errors


class Test_Place_errors(unittest.TestCase):
    def setUp(self):
        self.hbnb_command = HBNBCommand()

    def getCommandOutput(self, command):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(command)
            return mock_stdout.getvalue().strip()

    def test_create_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("create")
            self.assertEqual(output, "** class name missing **")

    def test_create_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("create MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show")
            self.assertEqual(output, "** class name missing **")

    def test_show_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_id_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show Place")
            self.assertEqual(output, "** instance id missing **")

    def test_show_id_not_found(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show Place Berlin")
            self.assertEqual(output, "** no instance found **")

    def test_destroy_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy")
            self.assertEqual(output, "** class name missing **")

    def test_destroy_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_instance_id_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy Place")
            self.assertEqual(output, "** instance id missing **")

    def test_destroy_no_instance_found(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy Place Berlin")
            self.assertEqual(output, "** no instance found **")

    def test_all_with_class_name(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("all Place")
            self.assertNotEqual(output, "** class doesn't exist **")

    def test_all_nonexistent_class(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("all MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update")
            self.assertEqual(output, "** class name missing **")

    def test_update_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_instance_id_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update Place")
            self.assertEqual(output, "** instance id missing **")

    def test_update_no_instance_found(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update Place Berlin")
            self.assertEqual(output, "** no instance found **")

    def test_update_attribute_name_missing(self):
        to_update = Place()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput(f"update Place {to_update.id}")
            self.assertEqual(output, "** attribute name missing **")

    def test_update_value_missing(self):
        to_update = Place()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput(
                f"update Place {to_update.id} name")
            self.assertEqual(output, "** value missing **")


# Test City
class TestConsoleWithCity(unittest.TestCase):
    def setUp(self):
        self.hbnb_command = HBNBCommand()

    def getCommandOutput(self, command):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(command)
            return mock_stdout.getvalue().strip()

    def test_create_city(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("create City")
            self.assertTrue(output is not None and len(output) > 0)

    def test_show_city(self):
        city_instance = City()
        city_id = city_instance.id
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput(f"show City {city_id}")
            expected_str = str(city_instance)
            self.assertEqual(expected_str, output)

    def test_destroy_city(self):
        city_instance = City()
        city_id = city_instance.id
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(f"destroy City {city_id}")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 0)

    def test_all_city(self):
        city_instance = City()
        city_id = city_instance.id
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(f"all City")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(str(city_instance) in output)

    def test_update_city(self):
        city_instance = City()
        city_id = city_instance.id
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(
                f"update City {city_id} name 'New York'")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 0)

# Test City Errors


class Test_City_errors(unittest.TestCase):
    def setUp(self):
        self.hbnb_command = HBNBCommand()

    def getCommandOutput(self, command):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(command)
            return mock_stdout.getvalue().strip()

    def test_create_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("create")
            self.assertEqual(output, "** class name missing **")

    def test_create_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("create MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show")
            self.assertEqual(output, "** class name missing **")

    def test_show_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_id_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show City")
            self.assertEqual(output, "** instance id missing **")

    def test_show_id_not_found(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show City Berlin")
            self.assertEqual(output, "** no instance found **")

    def test_destroy_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy")
            self.assertEqual(output, "** class name missing **")

    def test_destroy_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_instance_id_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy City")
            self.assertEqual(output, "** instance id missing **")

    def test_destroy_no_instance_found(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy City Berlin")
            self.assertEqual(output, "** no instance found **")

    def test_all_with_class_name(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("all City")
            self.assertNotEqual(output, "** class doesn't exist **")

    def test_all_nonexistent_class(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("all MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update")
            self.assertEqual(output, "** class name missing **")

    def test_update_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_instance_id_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update City")
            self.assertEqual(output, "** instance id missing **")

    def test_update_no_instance_found(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update City Berlin")
            self.assertEqual(output, "** no instance found **")

    def test_update_attribute_name_missing(self):
        to_update = City()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput(f"update City {to_update.id}")
            self.assertEqual(output, "** attribute name missing **")

    def test_update_value_missing(self):
        to_update = City()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput(
                f"update City {to_update.id} name")
            self.assertEqual(output, "** value missing **")


# Test Amenity
class TestConsoleWithAmenity(unittest.TestCase):
    def setUp(self):
        self.hbnb_command = HBNBCommand()

    def getCommandOutput(self, command):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(command)
            return mock_stdout.getvalue().strip()

    def test_create_amenity(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("create Amenity")
            self.assertTrue(output is not None and len(output) > 0)

    def test_show_amenity(self):
        amenity_instance = Amenity()
        amenity_id = amenity_instance.id
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput(f"show Amenity {amenity_id}")
            expected_str = str(amenity_instance)
            self.assertEqual(expected_str, output)

    def test_destroy_amenity(self):
        amenity_instance = Amenity()
        amenity_id = amenity_instance.id
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(f"destroy Amenity {amenity_id}")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 0)

    def test_update_amenity(self):
        amenity_instance = Amenity()
        amenity_id = amenity_instance.id
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(
                f"update Amenity {amenity_id} name 'New York'")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 0)

# Test Amenity Errors


class Test_Amenity_errors(unittest.TestCase):
    def setUp(self):
        self.hbnb_command = HBNBCommand()

    def getCommandOutput(self, command):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(command)
            return mock_stdout.getvalue().strip()

    def test_create_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("create")
            self.assertEqual(output, "** class name missing **")

    def test_create_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("create MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show")
            self.assertEqual(output, "** class name missing **")

    def test_show_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_id_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show Amenity")
            self.assertEqual(output, "** instance id missing **")

    def test_show_id_not_found(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("show Amenity Beds")
            self.assertEqual(output, "** no instance found **")

    def test_destroy_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy")
            self.assertEqual(output, "** class name missing **")

    def test_destroy_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_instance_id_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy Amenity")
            self.assertEqual(output, "** instance id missing **")

    def test_destroy_no_instance_found(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("destroy Amenity Beds")
            self.assertEqual(output, "** no instance found **")

    def test_all_with_class_name(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("all Amenity")
            self.assertNotEqual(output, "** class doesn't exist **")

    def test_all_nonexistent_class(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("all MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_class_name_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update")
            self.assertEqual(output, "** class name missing **")

    def test_update_class_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update MyModel")
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_instance_id_missing(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update Amenity")
            self.assertEqual(output, "** instance id missing **")

    def test_update_no_instance_found(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput("update Amenity Beds")
            self.assertEqual(output, "** no instance found **")

    def test_update_attribute_name_missing(self):
        to_update = Amenity()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput(f"update Amenity {to_update.id}")
            self.assertEqual(output, "** attribute name missing **")

    def test_update_value_missing(self):
        to_update = Amenity()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            output = self.getCommandOutput(
                f"update Amenity {to_update.id} name")
            self.assertEqual(output, "** value missing **")


if __name__ == '__main__':
    unittest.main()
