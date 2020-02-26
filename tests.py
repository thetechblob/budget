import unittest
from services.data import Data


class TestServices(unittest.TestCase):

    def test_calculate_diff_returns_3(self):
        self.data = Data('budget')
        self.assertEqual(self.data.calculate_diff(), 3)


if __name__ == '__main__':
    unittest.main()
