import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBase(unittest.TestCase):
    """Tests for Base Class"""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Reset FileStorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)


if __name__ == '__main__':
    unittest.main()
