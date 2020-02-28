import unittest

loader = unittest.TestLoader()
runner = unittest.TextTestRunner()
suite = loader.discover(start_dir="./")
runner.run(suite)
