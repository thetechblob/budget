import unittest
import pandas as pd
from pymongo import MongoClient
import sys

sys.path.insert(0, "..\\src\\services")

from database import Data


class DatabaseTests(unittest.TestCase):

    def setUp(self):
        self.db_name = "unittest"
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client[self.db_name]
        self.record = pd.DataFrame(
            dict(Date='2020-01-18', Description='shell canal walk milnerton za *', Account='Kredietkaart',
                 Amount=-23.0, Labels=0), index=[0])

    def tearDown(self):
        self.client.drop_database(self.db_name)

    def test_db_write_transaction_does_not_throw_exception(self):
        data = Data(self.db_name)
        raised = False

        try:
            data.persist_classified(self.record)
        except:
            raised = True

        self.assertFalse(raised, 'Exception raised trying to write to ' + self.db_name)

    def test_db_read_transaction_return_correct_result(self):
        data = Data(self.db_name)
        data.persist_classified(self.record)
        record = data.get_classified()

        result = record["Date"][0] == self.record["Date"][0] and \
                 record['Description'][0] == self.record['Description'][0] and \
                 record['Amount'][0] == self.record['Amount'][0]

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
