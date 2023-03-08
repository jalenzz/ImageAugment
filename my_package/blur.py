import os
import cv2
import shutil

'''
Gaussian Blur
'''
def blur(image, image_name, save_dir):
    blur_image = cv2.GaussianBlur(image, (7, 7), 0)
    save_path = os.path.join(save_dir, image_name + '_blur.jpg')
    cv2.imwrite(save_path, blur_image)
    print(save_path, 'saved')

def save_blur_label(name, raw_label_path, label_save_dir):
    blur_label = os.path.join(label_save_dir, name + "_blur.txt")
    if not os.path.exists(label_save_dir):
        os.makedirs(label_save_dir)
    shutil.copyfile(raw_label_path, blur_label)
    print(blur_label, 'saved')
