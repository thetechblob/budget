# File handling functions
import pandas as pd


class FileHandler:

    def read_csv(self, file_name, skip_rows=2):
        df = pd.read_csv(file_name, skiprows=skip_rows)
        df = df[['Date', 'Description', 'Account', 'Amount', 'Notes']]
        df.rename(columns={'Notes': 'Labels'}, inplace=True)
        return df

    def read_seed_csv(self, file_name):
        return self.read_csv(file_name, skip_rows=0)

