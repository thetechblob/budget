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
        self.file_name = "csv_test_file.csv"
        self.seed_file = "seed_test_file.csv"
        self.incorrect_seed = "seed_test_file_1.csv"
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client[self.db_name]

    def tearDown(self):
        self.client.drop_database(self.db_name)

    def test_update_new_transactions_on_execute_returns_correct_record_count(self):
        self.db["transactions"].delete_many({})
        controller = Controller(self.db_name)

        result = controller.update_new_transactions(self.file_name)

        self.assertEqual(result, 90)

    def test_seed_db_on_execute_returns_correct_record_count(self):
        controller = Controller(self.db_name)

        result = controller.seed_database(self.seed_file)

        self.assertEqual(result, 7899)

    def test_seed_db_with_wrong_csv_format_throws_exception(self):
        controller = Controller(self.db_name)

        self.assertRaises(KeyError, controller.seed_database, self.incorrect_seed)


if __name__ == '__main__':
    unittest.main()
