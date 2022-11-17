import tensorflow as tf

def conv_block(input):
    output = tf.keras.layers.Conv2D(32, 3, padding = 'same', activation = 'relu')(input)
    output = tf.keras.layers.BatchNormalization()(output)
    output = tf.keras.layers.MaxPool2D(2)(output)
            
    output = tf.keras.layers.Conv2D(64, 3, padding = 'same', activation = 'relu')(output)
    output = tf.keras.layers.BatchNormalization()(output)
    output = tf.keras.layers.MaxPool2D(2)(output)
            
    output = tf.keras.layers.Conv2D(128, 6, padding = 'valid', activation = 'relu')(output)
    output = tf.keras.layers.BatchNormalization()(output)
    output = tf.keras.layers.MaxPool2D(2)(output)
                
    output = tf.keras.layers.Conv2D(128, 6, padding = 'valid', activation = 'relu')(output)
    output = tf.keras.layers.BatchNormalization()(output)
    output = tf.keras.layers.MaxPool2D(2)(output)
    return output

def regression_block(input):
    output = tf.keras.layers.Flatten()(input)
    output = tf.keras.layers.Dense(1024, activation = 'relu')(output)
    output = tf.keras.layers.Dense(512, activation = 'relu')(output)
    output = tf.keras.layers.Dense(2, name = 'boundary box')(output)
    return output

def classification_block(input):
    output = tf.keras.layers.Flatten()(input)
    output = tf.keras.layers.Dense(1024, activation = 'relu')(output)
    output = tf.keras.layers.Dense(512, activation = 'relu')(output)
    output = tf.keras.layers.Dense(6, activation = 'softmax', name = 'class')(output)
    return output
