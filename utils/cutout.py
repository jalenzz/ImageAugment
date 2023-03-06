import os
import cv2
import shutil
import numpy as np

'''
Randomly pick out four positions
Fill with black/color rectangles
'''
def cutout(image, image_name, save_dir):
    min_size_ratio, max_size_ratio = 0.1, 0.3
    channel_wise = False
    max_crop = 4
    replacement=0

    size = np.array(image.shape[:2])
    mini, maxi = min_size_ratio * size, max_size_ratio * size
    cutout_image = image
    for _ in range(max_crop):
        # random size
        h = np.random.randint(mini[0], maxi[0])
        w = np.random.randint(mini[1], maxi[1])
        # random place
        shift_h = np.random.randint(0, size[0] - h)
        shift_w = np.random.randint(0, size[1] - w)

        if channel_wise:
            c = np.random.randint(0, image.shape[-1])
            cutout_image[shift_h:shift_h+h, shift_w:shift_w+w, c] = replacement
        else:
            cutout_image[shift_h:shift_h+h, shift_w:shift_w+w] = replacement

    save_path = os.path.join(save_dir, image_name + '_cutout.jpg')
    cv2.imwrite(save_path, cutout_image)
    print(save_path, 'saved')

def save_cutout_label(name, raw_label_path, label_save_dir):
    cutout_label = os.path.join(label_save_dir, name + "_cutout.txt")
    shutil.copyfile(raw_label_path, cutout_label)
    print(cutout_label, 'saved')
