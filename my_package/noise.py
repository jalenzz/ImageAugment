import os
import cv2
import shutil
import numpy as np

'''
Add noise to the image
Randomly generate 5000 salt and 5000 pepper
'''
def add_noise(image, image_name, save_dir):
    rows, cols, channel = image.shape
    noise_image = image
    for i in range(5000):
        x = np.random.randint(0,rows)
        y = np.random.randint(0,cols)
        noise_image[x,y,:] = 255
        x = np.random.randint(0,rows)
        y = np.random.randint(0,cols)
        noise_image[x,y,:] = 0

    save_path = os.path.join(save_dir, image_name + '_noise.jpg')
    cv2.imwrite(save_path, noise_image)
    print(save_path, 'saved')

def save_noise_label(name, raw_label_path, label_save_dir):
    noise_label = os.path.join(label_save_dir, name + "_noise.txt")
    shutil.copyfile(raw_label_path, noise_label)
    print(noise_label, 'saved')
