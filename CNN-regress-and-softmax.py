import tensorflow as tf

#batch size = 32
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