# File handling functions
import pandas as pd


class FileHandler:

    def read_csv(self, file_name):
        df = pd.read_csv(file_name, skiprows=2)
        df = df[['Date', 'Description', 'Account', 'Amount', 'Notes']]
        df.rename(columns={'Notes': 'Labels'}, inplace=True)
        return df

