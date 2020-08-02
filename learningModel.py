import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Dense

from numpy import loadtxt
import os
#import tensorflow_hub as hub
import numpy as np
print("bruh")



filePath = 'data'
csvEnding = '.csv'
dataCount = 10000


data = loadtxt(filePath+"_"+str(dataCount)+csvEnding, delimiter=',')

model = Sequential()
model.add(Dense(12, input_dim=2, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

X = data[:,2:4]
y = data[:,1]

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X, y, epochs=150, batch_size=10)

_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))