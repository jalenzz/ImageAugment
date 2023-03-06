import os
import cv2
import shutil
import numpy as np

'''
Image vignetting
'''
def vignetting(image, image_name, save_dir):
    random_sign = False
    ratio_min_dist = 0.2
    range_vignette = np.array((0.2, 0.8))

    h, w = image.shape[:2]
    min_dist = np.array([h, w]) / 2 * np.random.random() * ratio_min_dist

    # create matrix of distance from the center on the two axis
    x, y = np.meshgrid(np.linspace(-w/2, w/2, w), np.linspace(-h/2, h/2, h))
    x, y = np.abs(x), np.abs(y)

    # create the vignette mask on the two axis
    x = (x - min_dist[0]) / (np.max(x) - min_dist[0])
    x = np.clip(x, 0, 1)
    y = (y - min_dist[1]) / (np.max(y) - min_dist[1])
    y = np.clip(y, 0, 1)

    # then get a random intensity of the vignette
    vignette = (x + y) / 2 * np.random.uniform(*range_vignette)
    vignette = np.tile(vignette[..., None], [1, 1, 3])

    sign = 2 * (np.random.random() < 0.5) * random_sign - 1
    vignetting_img = image * (1 + sign * vignette)

    save_path = os.path.join(save_dir, image_name + '_vignetting.jpg')
    cv2.imwrite(save_path, vignetting_img)
    print(save_path, 'saved')

def save_vignetting_label(name, raw_label_path, label_save_dir):
    vignetting_label = os.path.join(label_save_dir, name + "_vignetting.txt")
    shutil.copyfile(raw_label_path, vignetting_label)
    print(vignetting_label, 'saved')
