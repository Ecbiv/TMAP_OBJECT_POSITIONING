import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense, Input, Flatten, Conv2D, MaxPool2D, BatchNormalization


def convolutional_block(input):
    output = Conv2D(filters = 16, kernel_size = (3,3), padding = 'same', activation = 'relu')(input)
    output = BatchNormalization()(output)
    output = MaxPool2D(pool_size=(2,2))(output)
    output = Conv2D(filters = 32, kernel_size = (3,3), padding = 'same', activation = 'relu')(output)
    output = BatchNormalization()(output)
    output = MaxPool2D(pool_size=(2,2))(output)
    return output

def regression_block_forward(input):
    output = Flatten()(input)
    output = Dense(1024, activation = 'relu')(output)
    output = Dense(512, activation = 'relu')(output)
    output = Dense(2, name = 'boundary_box')(output)
    return output

def classification_block_forward(input):
    output = Flatten()(input)
    output = Dense(1024, activation = 'relu')(output)
    output = Dense(512, activation = 'relu')(output)
    output = Dense(6, activation = 'softmax', name = 'class')(output)
    return output
