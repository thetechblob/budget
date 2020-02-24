import pymongo as mongo


class Data:

    def __init__(self, name):
        client = mongo.MongoClient("mongodb://localhost:27017")
        self._db = client[name]
        pass

    def read_transactions(self):
        pass

    def persist_transactions(self):
        pass


data = Data("budget")
