import pymongo as mongo
import pandas as pd
import hashlib


class Data:

    def __init__(self, name):
        client = mongo.MongoClient("mongodb://localhost:27017")
        self._db = client[name]
        self._classified = "transactions"
        self._unclassified = "unclassified"
        self._prediction = "prediction"

    def __persist_records(self, collection, records, seed=False):
        unique_records = records if seed else self.__filter(records)
        if unique_records.shape[0] > 0:
            self._db[collection].insert_many((unique_records.astype('str')).to_dict('records'))
        return unique_records.shape[0]

    def __get_hash_keys(self, records):
        keys = pd.DataFrame(records.apply(lambda x: self.__get_hash_key(x), axis=1))
        keys.columns = ["hash_key"]
        return keys

    @staticmethod
    def __get_hash_key(record):
        return hashlib.md5((str(record[0]) + str(record[1]) + str(record[2])).encode('utf-8')).hexdigest()

    def __filter(self, records):
        current_records = self.get_classified()
        merged_records = current_records.merge(records, on="hash_key", how="outer", indicator=True) \
            .query('_merge == "right_only"')
        unique_records = self.__select_coloumns(merged_records)
        return unique_records

    @staticmethod
    def __select_coloumns(unique_records):
        unique_records = unique_records[["Date_y", "Description_y", "Account_y", "Amount_y", "Labels_y", "hash_key"]] \
            .rename(columns={"Date_y": "Date", "Description_y": "Description", "Account_y": "Account",
                             "Amount_y": "Amount", "Labels_y": "Labels"})
        return unique_records

    def __get_records(self, collection):
        df = pd.DataFrame(self._db[collection].find({}))
        if df.shape[0] <= 0:
            return df
        df[["Labels"]] = df[["Labels"]].astype(int)
        df[["Amount"]] = df[["Amount"]].astype(float)
        return pd.DataFrame(df.iloc[:, 1:])

    def get_classified(self):
        return self.__get_records(collection=self._classified)

    def get_unclassified(self):
        return self.__get_records(collection=self._unclassified)

    def get_range(self, collection, start, end):
        df = pd.DataFrame(self._db[collection].find({}))
        df = df[df["Date"] >= start]
        df = df[df["Date"] <= end]
        return df

    def persist_classified(self, records):
        return self.__persist_records(collection=self._classified, records=records)

    def persist_unclassified(self, records):
        records["Labels"] = "0"
        records["hash_key"] = self.__get_hash_keys(records)
        self._db[self._unclassified].delete_many({})
        return self.__persist_records(collection=self._unclassified, records=records)

    def persist_prediction(self, records):
        self._db[self._prediction].delete_many({})
        return self.__persist_records(collection=self._prediction, records=records)

    def seed_transactions(self, records):
        self._db[self._classified].delete_many({})
        records["hash_key"] = self.__get_hash_keys(records)
        return self.__persist_records(collection=self._classified, records=records, seed=True)
