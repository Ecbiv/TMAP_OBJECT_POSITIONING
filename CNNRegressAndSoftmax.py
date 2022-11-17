import tensorflow as tf
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense, Input, Flatten, Conv2D, MaxPool2D, BatchNormalization

model = Sequential([
    Input(shape=(32, 32, 3,)),
    Conv2D(filters = 6, kernel_size = (3,3), padding = 'same', activation = 'relu'),
    MaxPool2D(pool_size=(2,2)),
    Conv2D(filters = 16, kernel_size = (3,3), padding = 'same', activation = 'relu'),
    MaxPool2D(pool_size=(2,2)),
    Conv2D(filters = 120, kernel_size = (3,3), padding = 'same', activation = 'relu'),
    Flatten()
])




def regression_block(input):
    output = Flatten()(input)
    output = Dense(1024, activation = 'relu')(output)
    output = Dense(512, activation = 'relu')(output)
    output = Dense(2, name = 'boundary box')(output)
    return output

def classification_block(input):
    output = Flatten()(input)
    output = Dense(1024, activation = 'relu')(output)
    output = Dense(512, activation = 'relu')(output)
    output = Dense(6, activation = 'softmax', name = 'class')(output)
    return output

