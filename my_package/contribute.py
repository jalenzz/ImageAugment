import os
import cv2
import shutil

def contribute(images_dir, labels_dir, datasets_dir):
    images_list = os.listdir(images_dir)
    images_num = len(images_list)
    for index, image_name_with_extension in enumerate(images_list, 1):
        image_name_without_extension = os.path.splitext(image_name_with_extension)[0]
        image_path = os.path.join(images_dir, image_name_with_extension)
        label_path = os.path.join(labels_dir, image_name_without_extension + '.txt')
        image = cv2.imread(image_path)

        image_rate = index / images_num
        if image_rate <= 0.7:
            image_save_path = os.path.join(datasets_dir, 'images', 'train', image_name_with_extension)
            label_save_dir = os.path.join(datasets_dir, 'labels', 'train')
            label_save_path = os.path.join(label_save_dir, image_name_without_extension + '.txt')
        elif image_rate <= 0.9:
            image_save_path = os.path.join(datasets_dir, 'images', 'val', image_name_with_extension)
            label_save_dir = os.path.join(datasets_dir, 'labels', 'val')
            label_save_path = os.path.join(label_save_dir, image_name_without_extension + '.txt')
        else:
            image_save_path = os.path.join(datasets_dir, 'images', 'test', image_name_with_extension)
            label_save_dir = os.path.join(datasets_dir, 'labels', 'test')
            label_save_path = os.path.join(label_save_dir, image_name_without_extension + '.txt')

        cv2.imwrite(image_save_path, image)
        print(image_save_path, 'saved')
        if not os.path.exists(label_save_dir):
            os.makedirs(label_save_dir)
        shutil.copyfile(label_path, label_save_path)
        print(label_save_path, 'saved')
