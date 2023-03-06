import os
import shutil

def copy_class(befor_dir, after_dir):
    befor_path = os.path.join(befor_dir, 'classes.txt')
    after_path = os.path.join(after_dir, 'classes.txt')
    if not os.path.exists(after_dir):
        os.makedirs(after_dir)
    shutil.copyfile(befor_path, after_path)
    print(after_path, 'saved')

def creat_dir(reshape_dir, aug_save_dir, datasets_dir):
    reshape_images_dir = [os.path.join(reshape_dir, 'images')]
    reshape_labels_dir = [os.path.join(reshape_dir, 'labels')]
    aug_images_save_dir = [os.path.join(aug_save_dir, 'images')]
    aug_labels_save_dir = [os.path.join(aug_save_dir, 'labels')]
    datasets_train_images_save_dir = [os.path.join(datasets_dir, 'images', 'train')]
    datasets_train_labels_save_dir = [os.path.join(datasets_dir, 'labels', 'train')]
    datasets_val_images_save_dir = [os.path.join(datasets_dir, 'images', 'val')]
    datasets_val_labels_save_dir = [os.path.join(datasets_dir, 'labels', 'val')]
    datasets_test_images_save_dir = [os.path.join(datasets_dir, 'images', 'test')]
    datasets_test_labels_save_dir = [os.path.join(datasets_dir, 'labels', 'test')]

    path_list = (reshape_images_dir + reshape_labels_dir + aug_images_save_dir + aug_labels_save_dir +
                datasets_train_images_save_dir + datasets_train_labels_save_dir +
                datasets_val_images_save_dir + datasets_val_labels_save_dir +
                datasets_test_images_save_dir + datasets_test_labels_save_dir)

    for path in path_list:
        if not os.path.exists(path):
            os.makedirs(path)
            print('creat', path)
        else:
            print(path, 'exists')