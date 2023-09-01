import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def wypisz(dane):
    for i in dane:
        yield i
    
def importing():
#pobranie danych
    data=tf.keras.datasets.mnist
    (train_images, train_labels), (test_images, test_labels) = data.load_data()

    #konwersja danych na typ float<=1
    train_images=train_images/255.0
    test_images=test_images/255.0

    #budowanie modelu
    model = tf.keras.models.Sequential([
      tf.keras.layers.Flatten(input_shape=(28, 28)),
      tf.keras.layers.Dense(128, activation='relu'),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(10)
    ])
    predictions = model(train_images[:1]).numpy()
    return predictions

def test():
    predictions=importing()

    while True:
        try:
            for i in predictions:
                x=yield i
        except StopIteration:
            break
        print(x)
