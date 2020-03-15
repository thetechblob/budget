from abc import ABC, abstractmethod


class Classifier(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_train_accuracy(self):
        pass

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def classify(self):
        pass
