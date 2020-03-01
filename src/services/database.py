import pymongo as mongo
import pandas as pd


class Data:

    def __init__(self, name):
        client = mongo.MongoClient("mongodb://localhost:27017")
        self._db = client[name]

    def read_transactions(self):
        df = pd.DataFrame(self._db["transactions"].find({}))
        df[["Labels"]] = df[["Labels"]].astype(int)
        df[["Amount"]] = df[["Amount"]].astype(float)
        return df

    def persist_transactions(self, records):
        self._db["transactions"].insert_many((records.astype('str')).to_dict('records'))
        return self._db["transactions"].count_documents({})

    def calculate_diff(self):
        return 5


data = Data("budget")
