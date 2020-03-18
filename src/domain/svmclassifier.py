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
        self.name = "SVM Classifier"
        self.train_accuracy = 0
        self._model = None

    def __prepare_data(self, df):
        df = self.__regular_substitution(df)
        df = self.__to_lower(df)
        return np.array(df['Description']), np.array(df['Labels'])

    def __regular_substitution(self, df):
        for i in range(df.shape[0]):
            df.loc[(i, "Description")] = re.sub(
                r"\d", " ", df.loc[(i, "Description")])
        return df

    def __to_lower(self, df):
        for i in range(df.shape[0]):
            tokens = word_tokenize(df.loc[(i, "Description")])
            tokens = [str(token).lower() for token in tokens]
            df.loc[(i, "Description")] = " ".join(tokens)
        return df

    def __train(self, X, y):
        estimators = [('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', SGDClassifier(
            loss='hinge', penalty='l2', alpha=1e-3, random_state=42, max_iter=50, tol=0.0001))]
        model = Pipeline(estimators)
        return model.fit(X, y)

    def __update_records_with_class(self, df, labels):
        df["Labels"] = labels
        df["Labels"] = df["Labels"].astype("int32").astype("str")
        return df

    def get_name(self):
        return self.name

    def get_train_accuracy(self):
        return self.train_accuracy

    def train(self, df):
        train_X, train_y = self.__prepare_data(df)
        self._model = self.__train(train_X, train_y)
        classification = self._model.predict(train_X)
        self.train_accuracy = accuracy_score(train_y, classification)

    def classify(self, df):
        if df.shape[0] <= 0:
            raise ValueError("Classification failed.  Empty dataframe.")
        test_X, _ = self.__prepare_data(df)
        labels = self._model.predict(test_X)
        df = self.__update_records_with_class(df, labels)
        return df
