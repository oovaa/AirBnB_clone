import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.hbnb_command = HBNBCommand()

    def assertCommandOutput(self, command):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(command)
            return mock_stdout.getvalue().strip()

    def test_help(self):
        help_message = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
        """
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd("help")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(help_message in output)

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
            self.hbnb_command.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)  # Length of UUID

            # Verify that the instance is actually created
            key = f"BaseModel.{output}"
            self.assertTrue(key in storage.all())

    def test_show(self):
        base_model = BaseModel()
        base_model.save()

        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(f"show BaseModel {base_model.id}")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(str(base_model) in output)

    # Add similar test methods for other commands (destroy, all, update, count)...

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd("all BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue("BaseModel" in output)

    def test_update(self):
        base_model = BaseModel()
        base_model.save()

        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(
                f"update BaseModel {base_model.id} name 'New Name'")
            output = mock_stdout.getvalue().strip()
