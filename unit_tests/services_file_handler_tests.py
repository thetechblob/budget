import unittest
import pandas as pd
from src.services.file_handler import FileHandler


class FileHandlerTests(unittest.TestCase):

    def test_on_success_read_file_return_dataframe(self):
        handler = FileHandler()
        result = handler.read_transactions("C:\\Users\\gpaul\\Documents\\repos\\budget\\unit_tests\\test_csv.csv")

        self.assertIsInstance(result, pd.DataFrame)
