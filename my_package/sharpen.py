import os
import cv2
import shutil
import numpy as np

'''
Image sharpening
'''
def sharpen(image, image_name, save_dir):
    identity_array = np.array([[0, 0, 0],
                               [0, 1, 0],
                               [0, 0, 0]])
    sharpen_array = np.array([[ 0, -1,  0],
                              [-1,  4, -1],
                              [ 0, -1,  0]]) / 4
    max_center = 4
    sharp = sharpen_array * np.random.random() * max_center
    kernel = identity_array + sharp

    sharpen_image = cv2.filter2D(image, -1, kernel)
    save_path = os.path.join(save_dir, image_name + '_sharpen.jpg')
    cv2.imwrite(save_path, sharpen_image)
    print(save_path, 'saved')

def save_sharpen_label(name, raw_label_path, label_save_dir):
    sharpen_label = os.path.join(label_save_dir, name + "_sharpen.txt")
    shutil.copyfile(raw_label_path, sharpen_label)
    print(sharpen_label, 'saved')
