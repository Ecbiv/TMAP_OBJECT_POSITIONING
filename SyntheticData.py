import glob
import numpy as np
import cv2
from PIL import Image

def get():
    synthetic_data = []
    #---------[BEGIN IMAGE PREPROCESSING]
    DOB_images = [cv2.imread(file, cv2.IMREAD_GRAYSCALE) for file in glob.glob("./original_DOB_images/*.png")]
    BG_images = [cv2.imread(file, cv2.IMREAD_GRAYSCALE) for file in glob.glob("./random_BG_IMG/n_data/*.jpg")]
    #---------[END IMAGE PREPROCESSING]

    for j in range(len(DOB_images)):
        for i in range(len(BG_images)):
            bg_img = BG_images[i]
            background = Image.fromarray(BG_images[i])
            larger_dimension_for_DOB = max(bg_img.shape[0], bg_img.shape[1])
            upper_limit = int(np.ceil(larger_dimension_for_DOB*0.1))
            lower_limit = int(np.ceil(larger_dimension_for_DOB*0.05))
            square_dimension = np.random.randint(lower_limit, upper_limit)
            foreground = cv2.resize(DOB_images[j], (square_dimension, square_dimension), interpolation=cv2.INTER_LINEAR)
            foreground = Image.fromarray(foreground)
            foreground.putalpha(255)
            upper_limit_placement = int(np.ceil(larger_dimension_for_DOB))
            lower_limit_placement = int(np.ceil(larger_dimension_for_DOB))
            background.paste(foreground, (np.random.randint(0, lower_limit_placement), np.random.randint(0, upper_limit_placement)), foreground)
            background = np.asarray(background)
            synthetic_data.append(background)
    return np.array(synthetic_data)

