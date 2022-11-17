import glob
import numpy as np
import cv2
from PIL import Image

def combine(background_images_path, foreground_images_path):
    """
    @Desc: Foreground objects are randomly placed into Background objects.
    @PARAM: background_images_path (Str)
                - A path to a folder of images that will be used as background images
            foreground_images_path (Str)
                - A path to a folder of images that will be placed onto the background images
    @Returns: An array of arrays such that [[combined image data, path to foreground file, coordinates of placed foreground object]]
    """
    synthetic_data = []
    #---------[BEGIN IMAGE PREPROCESSING]
    DOB_images = [[cv2.imread(file, cv2.IMREAD_GRAYSCALE), str(file)] for file in glob.glob(foreground_images_path)]
    BG_images = [cv2.imread(file, cv2.IMREAD_GRAYSCALE) for file in glob.glob(background_images_path)]
    #---------[END IMAGE PREPROCESSING]
    for j in range(len(DOB_images)):
        for i in range(len(BG_images)):
            bg_img = BG_images[i]
            background = Image.fromarray(BG_images[i])
            larger_dimension_for_DOB = max(bg_img.shape[0], bg_img.shape[1])
            upper_limit = int(np.ceil(larger_dimension_for_DOB*0.1))
            lower_limit = int(np.ceil(larger_dimension_for_DOB*0.05))
            square_dimension = np.random.randint(lower_limit, upper_limit)
            foreground = cv2.resize(DOB_images[j][0], (square_dimension, square_dimension), interpolation=cv2.INTER_LINEAR)
            foreground = Image.fromarray(foreground)
            foreground.putalpha(255)
            upper_limit_placement = int(np.ceil(larger_dimension_for_DOB))
            lower_limit_placement = int(np.ceil(larger_dimension_for_DOB))
            placement = (np.random.randint(0, lower_limit_placement), np.random.randint(0, upper_limit_placement))
            background.paste(foreground, placement , foreground)
            background = np.asarray(background)
            synthetic_data.append([background, DOB_images[j][1], placement])
    return np.array(synthetic_data)