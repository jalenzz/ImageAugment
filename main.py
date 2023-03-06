from utils.reshape import *
from utils.copy import *
from utils.blur import *
from utils.contrast import *
from utils.cutout import *
from utils.flip import *
from utils.lightness import *
from utils.sharpen import *
from utils.vignetting import *
from utils.contribute import *

raw_images_dir = './data/raw/images'
raw_labels_dir = './data/raw/labels'
reshape_dir = './data/reshaped/'
reshaped_images_dir = './data/reshaped/images'
reshaped_labels_dir = './data/reshaped/labels'
aug_save_dir = 'data/after_augment'
aug_images_save_dir = 'data/after_augment/images'
aug_labels_save_dir = 'data/after_augment/labels'
datasets_dir = './data/datasets'
resize_height = 640
resize_width = 640

if __name__ == "__main__":

    creat_dir(reshape_dir, aug_save_dir, datasets_dir)

    reshape(raw_images_dir, reshaped_images_dir,
            raw_labels_dir, reshaped_labels_dir,
            resize_height, resize_width)

    copy_class(raw_labels_dir, aug_labels_save_dir)

    images_list = os.listdir(reshaped_images_dir)
    for image_name_with_extension in images_list:
        image_name = os.path.splitext(image_name_with_extension)[0]
        image_path = os.path.join(reshaped_images_dir, image_name_with_extension)
        raw_label_path = os.path.join(reshaped_labels_dir, image_name + '.txt')
        image = cv2.imread(image_path)

        image_save_path = os.path.join(aug_images_save_dir, image_name + '.jpg')
        label_save_path = os.path.join(aug_labels_save_dir, image_name + '.txt')
        cv2.imwrite(image_save_path, image)
        shutil.copyfile(raw_label_path, label_save_path)

        blur(image, image_name, aug_images_save_dir)
        save_blur_label(image_name, raw_label_path, aug_labels_save_dir)

        contrast(image, image_name, aug_images_save_dir)
        save_contrast_label(image_name, raw_label_path, aug_labels_save_dir)

        cutout(image, image_name, aug_images_save_dir)
        save_cutout_label(image_name, raw_label_path, aug_labels_save_dir)

        flip(image, image_name, aug_images_save_dir)
        save_flip_label(image_name, raw_label_path, aug_labels_save_dir)

        brightness(image, image_name, aug_images_save_dir)
        save_brightness_label(image_name, raw_label_path, aug_labels_save_dir)

        darkness(image, image_name, aug_images_save_dir)
        save_darkness_label(image_name, raw_label_path, aug_labels_save_dir)

        sharpen(image, image_name, aug_images_save_dir)
        save_sharpen_label(image_name, raw_label_path, aug_labels_save_dir)

        vignetting(image, image_name, aug_images_save_dir)
        save_vignetting_label(image_name, raw_label_path, aug_labels_save_dir)

    contribute(aug_images_save_dir, aug_labels_save_dir, datasets_dir)
