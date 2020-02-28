import unittest
import pandas as pd
import sys

sys.path.insert(
    0, "..\\src\\services")

from database import Data


class DatabaseTests(unittest.TestCase):

    def test_on_construct_without_database_name_raise_exception(self):
        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main()
