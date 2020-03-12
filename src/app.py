import sys

sys.path.insert(0, "..\\src\\domain")
sys.path.insert(0, "..\\src\\services")

from file_handler import FileHandler
from controller import Controller

controller = Controller("test")

# print(controller.update_new_transactions(r"C:\\Users\\gpaul\\Documents\\repos\\budget\\unit_tests\csv_test_file.csv"))
print(controller.update_new_transactions(r"C:\\Users\\paul.nel\\Documents\\repos\\budget\\unit_tests\csv_test_file.csv"))
