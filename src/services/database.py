import pymongo as mongo
import pandas as pd


class Data:

    def __init__(self, name):
        client = mongo.MongoClient("mongodb://localhost:27017")

        self._db = client[name]
        self._classified = "transactions"
        self._unclassified = "unclassified"
        self._prediction = "classified"

    def __persist_records(self, collection, records):
        self._db[collection].insert_many((records.astype('str')).to_dict('records'))
        return self._db[collection].count_documents({})

    def __read_records(self, collection):
        df = pd.DataFrame(self._db[collection].find({}))
        df[["Labels"]] = df[["Labels"]].astype(int)
        df[["Amount"]] = df[["Amount"]].astype(float)
        return df.iloc[:, 1:]

    def get_classified(self):
        return self.__read_records(collection=self._classified)

    def get_unclassified(self):
        return self.__read_records(collection=self._unclassified)

    def persist_classified(self, records):
        return self.__persist_records(collection=self._classified, records=records)

    def persist_unclassified(self, records):
        records["Labels"] = 0
        self._db[self._unclassified].delete_many({})
        return self.__persist_records(collection=self._unclassified, records=records)

    def persist_classification(self, records):
        self._db[self._prediction].delete_many({})
        return self.__persist_records(collection=self._prediction, records=records)

    def seed_transactions(self, records):
        self._db[self._classified].delete_many({})
        return self.__persist_records(collection=self._classified, records=records)
