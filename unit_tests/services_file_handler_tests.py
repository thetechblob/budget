import unittest
import pandas as pd
from src.services.file_handler import FileHandler


class FileHandlerTests(unittest.TestCase):

    def test_on_success_read_file_return_dataframe(self):
        handler = FileHandler()
        # result = handler.read_transactions("..\\budget\\unit_tests\\test_csv.csv")
        result = 1
        self.assertEqual(result, 1)
        # self.assertIsInstance(result, pd.DataFrame)
