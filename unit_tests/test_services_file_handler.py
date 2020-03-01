import unittest
import pandas as pd
import sys

sys.path.insert(
    0, "..\\src\\services")

from file_handler import FileHandler


class FileHandlerTests(unittest.TestCase):

    def test_on_success_read_file_return_dataframe(self):
        handler = FileHandler()

        result = handler.read_csv("csv_test_file.csv")
        self.assertIsInstance(result, pd.DataFrame)


if __name__ == '__main__':
    unittest.main()

