import tensorflow as tf
from tensorflow import keras
from keras.layers import Dense, Input, Flatten, Conv2D, MaxPool2D, BatchNormalization

def conv_block(input):
    output = Conv2D(32, 3, padding = 'same', activation = 'relu')(input)
    output = BatchNormalization()(output)
    output = MaxPool2D(2)(output)
            
    output = Conv2D(64, 3, padding = 'same', activation = 'relu')(output)
    output = BatchNormalization()(output)
    output = MaxPool2D(2)(output)
            
    output = Conv2D(128, 6, padding = 'valid', activation = 'relu')(output)
    output = BatchNormalization()(output)
    output = MaxPool2D(2)(output)
                
    output = Conv2D(128, 6, padding = 'valid', activation = 'relu')(output)
    output = BatchNormalization()(output)
    output = MaxPool2D(2)(output)
    return output

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

