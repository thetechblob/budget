from __future__ import absolute_import, division, print_function, unicode_literals

import time
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_datasets as tfds
from keras.preprocessing.text import Tokenizer
import matplotlib.pyplot as plt

print("Version: ", tf.__version__)
print("Eager mode: ", tf.executing_eagerly())
print("Hub version: ", hub.__version__)
print("GPU is", "available" if tf.config.experimental.list_physical_devices("GPU") else "NOT AVAILABLE")

raw_data = pd.read_csv('data/classified_transactions.csv')
shuffle_raw_data = raw_data.sample(frac=1, random_state=1).reset_index(drop=True)

features = raw_data.pop("Description")
labels = raw_data.pop("Labels")

tokenizer = Tokenizer()
tokenizer.fit_on_texts(features)
features = tokenizer.texts_to_matrix(features, mode="tfidf")

train = int(0.9*len(raw_data))
train_data = tf.data.Dataset.from_tensor_slices((features[:train], labels[:train]))
test_data = tf.data.Dataset.from_tensor_slices((features[train:], labels[train:]))

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

model.compile(optimizer='adam',
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy'])

start = time.clock()
history = model.fit(train_data.shuffle(144).batch(1),
                    epochs=30,
                    verbose=1)
end = time.clock()
results = model.evaluate(test_data.batch(1), verbose=2)
print(results)

for name, value in zip(model.metrics_names, results):
    print("%s: %.3f" % (name, value))

print(shuffle_raw_data["Description"][train:])
print(model.predict_classes(features[train:]))

print('start: {}'.format(start))
print('end: {}'.format(end))
print('duration: {}'.format(end-start))

fig, ax = plt.subplots()
ax.plot(history.history['accuracy'])
ax.plot(history.history['loss'])
plt.show()

