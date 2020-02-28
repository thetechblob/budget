import unittest
import pandas as pd
import sys

sys.path.insert(
    0, "..\\src\\services")

from database import Data


class DatabaseTests(unittest.TestCase):

    def test_on_construct_without_databse_name_rais_exception(self):
        self.assertRaises(TypeError, Data(), 'name')


if __name__ == '__main__':
    unittest.main()
