import sys

sys.path.insert(0, "..\\src\\domain")
sys.path.insert(0, "..\\src\\services")

from controller import Controller
from svmclassifier import SVMClassifier

db_name = "test"
classification_csv_file = "../data/classified_transactions.csv"

classifier = SVMClassifier()
controller = Controller(classifier, db_name, classification_csv_file)

# controller.seed_database("../data/seed_file.csv")
# controller.get_new_transactions("../data/transactions.csv")
# controller.classify_new_transactions()
# print(classifier.get_name(), classifier.get_train_accuracy())
# print(controller.confirm_csv_classification())
print(controller.get_nett_balance("2015-01-19", "2015-01-26"))
