import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense, Input, Flatten, Conv2D, MaxPooling2D, Dropout, BatchNormalization

def OHE_encoder(output):
    OHE = [0]*len(output)
    LABEL = max(output)
    output = list(output)
    LABEL_INDEX = output.index(LABEL)
    OHE[LABEL_INDEX] = 1
    return OHE

def convolutional_block(input):
    output = Conv2D(filters = 16, kernel_size = (3,3), padding = 'same', activation = 'relu')(input)
    output = BatchNormalization()(output)
    output = MaxPooling2D(pool_size=(2,2))(output)
    output = Conv2D(filters = 32, kernel_size = (3,3), padding = 'same', activation = 'relu')(output)
    output = BatchNormalization()(output)
    output = MaxPooling2D(pool_size=(2,2))(output)
    output = Conv2D(filters = 64, kernel_size = (6,6), padding = 'same', activation = 'relu')(output)
    output = BatchNormalization()(output)
    output = MaxPooling2D(pool_size=(2,2))(output)
    output = Conv2D(filters = 64, kernel_size = (6,6), padding = 'same', activation = 'relu')(output)
    output = BatchNormalization()(output)
    output = MaxPooling2D(pool_size=(2,2))(output)
    return output

def regression_block_forward(input):
    output = Flatten()(input)
    output = Dense(1024, activation = 'relu')(output)
    output = Dense(512, activation = 'relu')(output)
    output = Dropout(0.5)(output)
    output = Dense(1, name = 'Coordinates_Surface_Area')(output)
    return output

def getUntrainedModel(input_shape = (224, 224, 3)):
    input = Input(input_shape)
    x = convolutional_block(input)
    box_output = regression_block_forward(x)
    model = keras.Model(inputs=input, outputs = [box_output])
    model.compile(optimizer=tf.keras.optimizers.Adam(), loss={'Coordinates_Surface_Area': 'mean_squared_error'}, metrics={'Coordinates_Surface_Area': tf.keras.metrics.RootMeanSquaredError()})
    return model