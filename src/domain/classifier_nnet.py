from __future__ import absolute_import, division, print_function, unicode_literals

from IClassifier import IClassifier
import numpy as np
import pandas as pd
import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences


class NNetClassifier(IClassifier):

    def __init__(self):
        self._name = "Neural Net Classifier"
        self._train_accuracy = 0
        self._test_accuracy = 0
        self._model = None
        self._EPOCHS = 10
        self._BATCH = 4
        self._OPTIMIZER = 'adam'

        print("Version: ", tf.__version__)
        print("Eager mode: ", tf.executing_eagerly())
        print("GPU is", "available" if tf.config.experimental.list_physical_devices("GPU") else "NOT AVAILABLE")

    def __prepare_data(self, df, split=0.2):
        train = int((1 - split) * len(df))
        df = df.sample(frac=1).reset_index(drop=True)
        features = df["Description"]
        features = self.__tokenize_features(features)
        labels = df["Labels"]
        train_data = tf.data.Dataset.from_tensor_slices((features[:train], labels[:train]))
        test_data = tf.data.Dataset.from_tensor_slices((features[train:], labels[train:]))
        return train_data, test_data

    @staticmethod
    def __update_records_with_class(df, labels):
        df["Labels"] = labels
        df["Labels"] = df["Labels"].astype("int32").astype("str")
        return df

    @staticmethod
    def __compile_model(optimizer='adam'):
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Dense(32, activation='relu'))
        model.add(tf.keras.layers.Dropout(0.1))
        model.add(tf.keras.layers.Dense(32, activation='relu'))
        model.add(tf.keras.layers.Dropout(0.1))
        model.add(tf.keras.layers.Dense(32, activation='relu'))
        model.add(tf.keras.layers.Dropout(0.1))
        model.add(tf.keras.layers.Dense(32, activation='relu'))
        model.add(tf.keras.layers.Dropout(0.1))
        model.add(tf.keras.layers.Dense(32, activation='relu'))
        model.add(tf.keras.layers.Dropout(0.1))
        model.add(tf.keras.layers.Dense(32, activation='relu'))
        model.add(tf.keras.layers.Dropout(0.1))
        model.add(tf.keras.layers.Dense(32, activation='relu'))
        model.add(tf.keras.layers.Dense(32, activation='relu'))
        model.add(tf.keras.layers.Dense(1))
        model.compile(optimizer=optimizer,
                      loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                      metrics=['accuracy'])
        return model

    @staticmethod
    def __tokenize_features(features):
        tokenizer = Tokenizer(num_words=None, char_level=True, oov_token="UNK")
        tokenizer.fit_on_texts(features)
        feature_seq = tokenizer.texts_to_sequences(features)
        return pad_sequences(feature_seq, maxlen=50, padding="post")

    def get_name(self):
        return self._name

    def get_train_accuracy(self):

        return self._train_accuracy

    def get_test_accuracy(self):
        return self._test_accuracy

    def train(self, df):
        train_data, test_data = self.__prepare_data(df, split=0.2)
        self._model = self.__compile_model(optimizer=self._OPTIMIZER)
        self._model.fit(train_data.shuffle(8).batch(self._BATCH), epochs=self._EPOCHS, verbose=1)
        self._train_accuracy = self.__accuracy(train_data)
        self._test_accuracy = self.__accuracy(test_data)

    def __accuracy(self, data):
        results = self._model.evaluate(data.batch(self._BATCH), verbose=2)
        return results[1]

    def classify(self, df):
        features = df["Description"]
        features = self.__tokenize_features(features)
        labels = pd.DataFrame(self._model.predict_classes(features))
        return self.__update_records_with_class(df, labels)
