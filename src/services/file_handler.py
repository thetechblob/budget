# File handling functions
import pandas as pd


class FileHandler:

    def read_transactions(self, file_name):
        df = pd.read_csv(file_name)
        return df

    def print_test(self):
        print("Handled file")
