import unittest
from pymongo import MongoClient

import sys

sys.path.insert(0, '..\\src\\domain')
sys.path.insert(0, '..\\src\\services')

from database import Data
from file_handler import FileHandler
from controller import Controller


class ControllerTests(unittest.TestCase):

    def setUp(self):
        self.db_name = "unittest"
        self.file_name = 'csv_test_file.csv'
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client[self.db_name]

    def tearDown(self):
        self.client.drop_database(self.db_name)

    def test_update_new_transactions_on_execute_returns_correct_record_count(self):
        self.db["transactions"].remove({})
        controller = Controller(self.db_name)

        result = controller.update_new_transactions(self.file_name)

        self.assertEqual(result, 90)


if __name__ == '__main__':
    unittest.main()
