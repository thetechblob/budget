# class responsible for managing learning and data access between ui and services
import sys

sys.path.insert(0, "..\\src\\services")
from database import Data
from file_handler import FileHandler


class Controller:

    def __init__(self, db_name):
        self.data = Data(db_name)
        self.handler = FileHandler()

    def update_new_transactions(self, file_name):
        df = self.handler.read_csv(file_name)
        records = self.data.persist_transactions(df)
        return records
