import glob
import numpy as np
import tensorflow as tf
import cv2
from PIL import Image, ImageDraw


def combine(background_images_path, foreground_images_path, verbose=False):
    """
    @Desc: Foreground objects are randomly placed into Background objects.
    @PARAM: background_images_path (Str)
                - A path to a folder of images that will be used as background images
            foreground_images_path (Str)
                - A path to a folder of images that will be placed onto the background images
    @Returns: An array of arrays such that [[combined image data, path to foreground file, coordinates of placed foreground object, size of foreground object]]
              A dictionary of OHE labels for foreground images - keys: file_path, values: ohe_label
    """
    synthetic_data = []
    DOB_OHE = {}
    #---------[BEGIN IMAGE PREPROCESSING]
    DOB_images = np.array([np.array([cv2.imread(file), str(file)], dtype=object) for file in glob.glob(foreground_images_path)], dtype=object)
    BG_images = np.array([cv2.imread(file) for file in glob.glob(background_images_path)])
    #---------[END IMAGE PREPROCESSING]

    #---------[BEGIN OHE LABELLING OF FOREGROUND IMAGES]
    OHE = 0
    for file in glob.glob(foreground_images_path):
        OHE_LABEL = [0]*len(DOB_images)
        OHE_LABEL[OHE] = 1
        DOB_OHE[file] = OHE_LABEL
        OHE += 1
    #---------[END OHE LABELLING OF FOREGROUND IMAGES]   
    
    for j in range(len(DOB_images)):
        for i in range(len(BG_images)):
            bg_img = BG_images[i]
            background = Image.fromarray(BG_images[i])
            smaller_dimension_for_DOB = min(bg_img.shape[0], bg_img.shape[1])
            upper_limit = int(np.ceil(smaller_dimension_for_DOB*0.1))
            lower_limit = int(np.ceil(smaller_dimension_for_DOB*0.05))
            square_dimension = np.random.randint(lower_limit, upper_limit)
            foreground = cv2.resize(DOB_images[j][0], (square_dimension, square_dimension), interpolation=cv2.INTER_LINEAR)
            foreground = Image.fromarray(foreground)
            foreground.putalpha(255)
            upper_limit_placement = int(np.ceil(smaller_dimension_for_DOB))
            lower_limit_placement = int(np.ceil(smaller_dimension_for_DOB))
            placement = (np.random.randint(0, lower_limit_placement), np.random.randint(0, upper_limit_placement))
            background.paste(foreground, placement , foreground)
            background = np.asarray(background)
            synthetic_data.append([background, DOB_images[j][1], placement, square_dimension])
            if verbose:
                cv2.imshow("Current Combined Image", synthetic_data[-1][0])
                cv2.waitKey()
    return np.array(synthetic_data, dtype=object), DOB_OHE


def plot_bounding_box(image_set, pred_coords = None):
    """
    @Desc: Takes image_set produced by combine() and draws a box around the foreground object,
    @PARAM: image_set
                - the object returned by combine()
    @Returns: An array of arrays such that [[combined image data with drawn box around fg image, path to foreground file, coordinates of placed foreground object, size of foreground object]]
    """
    bounded_image_set = []
    for image in image_set:
        img_array, classification, coordinates, size = image[0], image[1], image[2], image[3]
        img_literal = Image.fromarray(img_array)
        draw = ImageDraw.Draw(img_literal)
        draw.rectangle((coordinates[0], coordinates[1], coordinates[0] + size, coordinates[1] + size), outline = 'blue', width = 2)
        true_rectangle = (coordinates[0], coordinates[1], coordinates[0] + size, coordinates[1] + size)
        if pred_coords:
            draw.rectangle((pred_coords[0], pred_coords[1], pred_coords[0] + size, pred_coords[1] + size), outline = 'red', width = 2)
        bounded_image_set.append([np.array(img_literal), classification, coordinates, size, true_rectangle])
    return np.array(bounded_image_set, dtype=object)
