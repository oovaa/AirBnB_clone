import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models import storage


class TestHBNBCommand(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
