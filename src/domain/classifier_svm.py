import re
import numpy as np
from IClassifier import IClassifier
from nltk import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score


class SVMClassifier(IClassifier):

    def __init__(self):
        self._name = "SVM Classifier"
        self._train_accuracy = 0
        self._test_accuracy = 0
        self._model = None

    @staticmethod
    def __regular_substitution(df):
        for i in range(df.shape[0]):
            df.loc[(i, "Description")] = re.sub(
                r"\d", " ", df.loc[(i, "Description")])
        return df

    @staticmethod
    def __to_lower(df):
        for i in range(df.shape[0]):
            tokens = word_tokenize(df.loc[(i, "Description")])
            tokens = [str(token).lower() for token in tokens]
            df.loc[(i, "Description")] = " ".join(tokens)
        return df

    @staticmethod
    def __train(X, y):
        estimators = [('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', SGDClassifier(
            loss='hinge', penalty='l2', alpha=1e-3, random_state=42, max_iter=50, tol=0.0001))]
        model = Pipeline(estimators)
        return model.fit(X, y)

    @staticmethod
    def __update_records_with_class(df, labels):
        df["Labels"] = labels
        df["Labels"] = df["Labels"].astype("int32").astype("str")
        return df

    def __prepare_data(self, df, split=0.2):
        df = self.__regular_substitution(df)
        df = self.__to_lower(df).sample(frac=1)
        train = int((1 - split) * len(df))
        return np.array(df['Description'][:train]), np.array(df['Labels'][:train]), \
               np.array(df['Description'][train:]), np.array(df['Labels'][train:])

    def get_name(self):
        return self._name

    def get_train_accuracy(self):
        return self._train_accuracy

    # TODO implement this
    def get_test_accuracy(self):
        return self._test_accuracy

    def train(self, df):
        train_X, train_y, test_X, test_y = self.__prepare_data(df, split=0.2)
        self._model = self.__train(train_X, train_y)
        self._train_accuracy = self.__get_accuracy(train_X, train_y)
        self._test_accuracy = self.__get_accuracy(test_X, test_y)

    def __get_accuracy(self, X, y):
        prediction = self._model.predict(X)
        return accuracy_score(y, prediction)

    def classify(self, df):
        if df.shape[0] <= 0:
            raise ValueError("Classification failed.  Empty dataframe.")
        data, _, _, _ = self.__prepare_data(df, split=0)
        labels = self._model.predict(data)
        return self.__update_records_with_class(df, labels)
