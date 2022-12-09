from tensorflow import keras
import tensorflow as tf
import numpy as np
import cv2
import csv

def main():
    img1 = np.array(cv2.imread("./CLASS_TRAINING_DATA/circle_left.jpg", cv2.IMREAD_UNCHANGED))
    img2 = np.array(cv2.imread("./CLASS_TRAINING_DATA/door_right.jpg", cv2.IMREAD_UNCHANGED))
    img1 = cv2.resize(img1, (224,224))
    img2 = cv2.resize(img2, (224,224))
    img1 = tf.keras.backend.constant(img1)
    img2 = tf.keras.backend.constant(img2)
    batch = []
    batch.append(img1)
    batch.append(img2)
    batch = np.array(batch)
    scaling_factor = 0.8738697
    img1 = np.array(cv2.imread("./CLASS_TRAINING_DATA/circle_left.jpg", cv2.IMREAD_UNCHANGED))
    img2 = np.array(cv2.imread("./CLASS_TRAINING_DATA/door_right.jpg", cv2.IMREAD_UNCHANGED))

    from PIL import Image

    img1 = Image.open("./CLASS_TRAINING_DATA/circle_left.jpg")
    img2 = Image.open("./CLASS_TRAINING_DATA/door_right.jpg")

    from math import floor

    new_shape = floor(3024*scaling_factor), floor(4032*scaling_factor)
    img2 = img2.resize(new_shape)
    result = Image.new(img2.mode, (3024, 4032), (0, 0, 255))
    result.paste(img2, (0,0))

    img2 = result.resize((1080, 1080))
    img1 = img1.resize((1080, 1080))
    img1_path = "./new_dir/circle_left.jpg"
    img2_path = "./new_dir/door_right.jpg"
    img1 = np.array(img1)
    img2 = np.array(img2)
    cv2.imwrite(img1_path, img1)
    cv2.imwrite(img2_path, img2)
    with open('sides.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow((img1_path, "circle"))
        writer.writerow((img2_path, "door"))

main()