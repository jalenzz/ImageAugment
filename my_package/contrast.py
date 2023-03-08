import os
import cv2
import shutil
import numpy as np
from PIL import Image

'''
Contrast transformation
'''
def contrast(image, image_name, save_dir):
    image = Image.fromarray(image)
    range_contrast=(-50, 50)
    contrast = np.random.randint(*range_contrast)
    contrast_img = image.point(lambda p: p * (contrast / 127 + 1) - contrast)

    save_path = os.path.join(save_dir, image_name + '_contrast.jpg')
    contrast_img = np.array(contrast_img)
    cv2.imwrite(save_path, contrast_img)
    print(save_path, 'saved')


def save_contrast_label(name, raw_label_path, label_save_dir):
    contrast_label = os.path.join(label_save_dir, name + "_contrast.txt")
    shutil.copyfile(raw_label_path, contrast_label)
    print(contrast_label, 'saved')
