import os
import shutil
from PIL import Image
from torchvision import transforms

def reshape(raw_image_dir, image_save_dir, raw_label_dir, label_save_dir, resize_weight, resize_width):
    raw_images_list = os.listdir(raw_image_dir)
    for index, image_name in enumerate(raw_images_list, 1):
        image_path = os.path.join(raw_image_dir, image_name)
        label_path = os.path.join(raw_label_dir, os.path.splitext(image_name)[0] + '.txt')
        image = Image.open(image_path)
        resize = transforms.Resize([resize_weight, resize_width])
        reshape_image = resize(image)

        image_save_name = f'{os.path.splitext(image_name)[0]}.jpg'
        label_save_name = f'{os.path.splitext(image_name)[0]}.txt'
        image_save_path = os.path.join(image_save_dir, image_save_name)
        label_save_path = os.path.join(label_save_dir, label_save_name)
        if not os.path.exists(image_save_dir):
            os.makedirs(image_save_dir)
        reshape_image.save(image_save_path)

        if not os.path.exists(label_save_dir):
            os.makedirs(label_save_dir)
        shutil.copyfile(label_path, label_save_path)

    print('reshape completed. save to', image_save_dir)