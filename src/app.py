import sys

sys.path.insert(0, "..\\src\\domain")
sys.path.insert(0, "..\\src\\services")

from controller import Controller
from classifier_svm import SVMClassifier
from classifier_nnet import NNetClassifier

db_name = "test"
seed_file = "../data/seed_file.csv"
new_transactions = "../data/transactions.csv"
classification_csv_file = "../data/classified_transactions.csv"

classifier = NNetClassifier()
# classifier = SVMClassifier()

controller = Controller(classifier, db_name, classification_csv_file)
controller.all_to_csv('../data/all_transactions.csv')
controller.seed_database(seed_file)
controller.get_new_transactions(new_transactions)
controller.classify_new_transactions()
print("\nClassifier: {} \nTraining Accuracy: {} \nTest Accuracy: {}".format(classifier.get_name(),
                                                                              classifier.get_train_accuracy(),
                                                                              classifier.get_test_accuracy()))
print(controller.get_nett_balance("2015-01-19", "2015-01-26"))
