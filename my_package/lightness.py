import os
import cv2
import shutil
import numpy as np
from PIL import Image

'''
Image brightness enhancement/reduction
'''
def brightness(image, image_name, save_dir):
    image = Image.fromarray(image)
    brightness = 1 + np.random.randint(1, 9) / 10
    brightness_img = image.point(lambda p: p * brightness)

    save_path = os.path.join(save_dir, image_name + '_brightness.jpg')
    brightness_img = np.array(brightness_img)
    cv2.imwrite(save_path, brightness_img)
    print(save_path, 'saved')

def darkness(image, image_name, save_dir):
    darkness = np.random.randint(1, 9) / 10
    darkness_img = image * darkness

    save_path = os.path.join(save_dir, image_name + '_darkness.jpg')
    cv2.imwrite(save_path, darkness_img)
    print(save_path, 'saved')

def save_brightness_label(name, raw_label_path, label_save_dir):
    brightness_label = os.path.join(label_save_dir, name + "_brightness.txt")
    shutil.copyfile(raw_label_path, brightness_label)
    print(brightness_label, 'saved')


def save_darkness_label(name, raw_label_path, label_save_dir):
    darkness_label = os.path.join(label_save_dir, name + "_darkness.txt")
    shutil.copyfile(raw_label_path, darkness_label)
    print(darkness_label, 'saved')
