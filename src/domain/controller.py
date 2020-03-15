# class responsible for managing learning and data access between ui and services
import sys

sys.path.insert(0, "..\\services")
from database import Data
from file_handler import FileHandler


class Controller:

    def __init__(self, classifier, db_name, class_csv_name):
        self.data = Data(db_name)
        self.handler = FileHandler()
        self.classifier = classifier
        self.class_csv = class_csv_name

    def update_new_transactions(self, file_name):
        df = self.handler.read_csv(file_name)
        return self.data.persist_unclassified(df)

    def seed_database(self, file_name):
        df = self.handler.read_seed_csv(file_name)
        return self.data.seed_transactions(df)

    def classify_new_transactions(self):
        self.__train_model()
        classified = self.__classify_new()
        self.__persist_classification(classified)

    def __train_model(self):
        train_data = self.data.get_classified()
        self.classifier.train(train_data)

    def __classify_new(self):
        return self.classifier.classify(self.data.get_unclassified())

    def __persist_classification(self, classified):
        self.data.persist_classification(classified)
        self.handler.write_csv(classified, self.class_csv)

    def confirm_csv_classification(self):
        df = self.handler.read_classified_csv(self.class_csv)
        return self.data.persist_classified(df)
