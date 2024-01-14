import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.hbnb_command = HBNBCommand()

    def assertCommandOutput(self, command):
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
            output = self.assertCommandOutput("create BaseModel")
            # Check if the output is a valid UUID
            self.assertTrue(len(output) == 36)

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd("create BaseModel")
            instance_id = mock_stdout.getvalue().strip()
            output = self.assertCommandOutput(f"show BaseModel {instance_id}")
            # Check if the instance details are in the output
            self.assertTrue(instance_id in output)

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd("create BaseModel")
            instance_id = mock_stdout.getvalue().strip()
            self.hbnb_command.onecmd(f"destroy BaseModel {instance_id}")
            output = self.assertCommandOutput(f"show BaseModel {instance_id}")
            # Check if the instance is deleted
            self.assertTrue("** no instance found **" in output)

    # Add similar test methods for other commands (all, update, count)...


if __name__ == '__main__':
    unittest.main()
