from abc import ABC, abstractmethod


class Classifier(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def classify(self):
        pass

