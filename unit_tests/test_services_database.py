import unittest
import pandas as pd
from pymongo import MongoClient
import sys

sys.path.insert(0, "..\\src\\services")
sys.path.insert(0, "..\\src\\domain")

from database import Data
from file_handler import FileHandler
from svmclassifier import SVMClassifier


class DatabaseTests(unittest.TestCase):

    def setUp(self):
        self.db_name = "unittest"
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client[self.db_name]
        self.seed_file = "seed_test_file.csv"
        self.classified = "classified_test_transactions.csv"
        self.record = pd.DataFrame(
            dict(Date='2018-12-04', Description='ibank payment to absa bank bridgiot', Account='Tjek',
                 Amount=-1380.0, Labels=0, hash_key='759076c6734fd66b737dbae1f1e8309f'), index=[0])

    def tearDown(self):
        self.client.drop_database(self.db_name)

    def test_persist_classified_with_new_records_returns_correct_diff_record_count(self):
        data = Data(self.db_name)
        handler = FileHandler()
        seed = handler.read_seed_csv(self.seed_file)
        data.seed_transactions(seed)
        new_data = handler.read_classified_csv(self.classified)

        result = data.persist_classified(new_data)

        self.assertEqual(144, result)

    def test_persist_classified_with_duplicate_records_returns_zero_diff_record_count(self):
        data = Data(self.db_name)
        handler = FileHandler()
        seed = handler.read_seed_csv(self.seed_file)
        data.seed_transactions(seed)
        new_data = handler.read_classified_csv(self.classified)
        data.persist_classified(new_data)

        result = data.persist_classified(new_data)

        self.assertEqual(0, result)


if __name__ == '__main__':
    unittest.main()
