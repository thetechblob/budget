import sys

sys.path.insert(0, "..\\src\\domain")
sys.path.insert(0, "..\\src\\services")

from file_handler import FileHandler
from controller import Controller
from svmclassifier import SVMClassifier

classifier = SVMClassifier()
db_name = "test"
classification_csv_file = "../data/classified_transactions.csv"

controller = Controller(classifier, db_name, classification_csv_file)
controller.seed_database("../data/seed_file.csv")
controller.classify_new_transactions()
print(classifier.name, classifier.train_accuracy)
print(controller.confirm_csv_classification())
