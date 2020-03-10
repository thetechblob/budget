# file to contain all ui relate requests
import sys
import os
package_path = os.path.split(os.path.abspath(__file__))[0]
sub_directories = package_path.count('\\')
print(sub_directories)
package_path = package_path.split('\\', -1)
print(package_path)
sys.path.insert(0, package_path)

import file_handler


def get_nett_for_range():
    handler = file_handler.FileHandler()
    df = handler.read_transactions('transactions.csv')
