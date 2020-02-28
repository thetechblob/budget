import unittest
import sys
from test_services_database import DatabaseTests

test_list = [DatabaseTests]
test_loader = unittest.TestLoader()

sys.path.insert(0, "C:\\Users\\Paul.Nel\\Documents\\repos\\budget")

newSuite = test_loader.discover(start_dir="/", pattern='test*.py', top_level_dir="../")

# newSuite = unittest.TestSuite(TestList)
runner = unittest.TextTestRunner()
runner.run(newSuite)
