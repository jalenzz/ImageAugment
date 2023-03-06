import os
import cv2

'''
Flip the image
'''

def flip(image, image_name, save_dir):
    flip_image_1 = cv2.flip(image,  0)
    flip_image_2 = cv2.flip(image,  1)
    flip_image_3 = cv2.flip(image, -1)

    rotate_image = cv2.rotate(image, 0)
    flip_image_5 = cv2.flip(rotate_image,  0)
    flip_image_6 = cv2.flip(rotate_image,  1)
    flip_image_7 = cv2.flip(rotate_image, -1)

    save_path1 = os.path.join(save_dir, image_name + '_flip1.jpg')
    save_path2 = os.path.join(save_dir, image_name + '_flip2.jpg')
    save_path3 = os.path.join(save_dir, image_name + '_flip3.jpg')
    save_path4 = os.path.join(save_dir, image_name + '_flip4.jpg')
    save_path5 = os.path.join(save_dir, image_name + '_flip5.jpg')
    save_path6 = os.path.join(save_dir, image_name + '_flip6.jpg')
    save_path7 = os.path.join(save_dir, image_name + '_flip7.jpg')

    cv2.imwrite(save_path1, flip_image_1)
    print(save_path1, 'saved')
    cv2.imwrite(save_path2, flip_image_2)
    print(save_path2, 'saved')
    cv2.imwrite(save_path3, flip_image_3)
    print(save_path3, 'saved')
    cv2.imwrite(save_path4, rotate_image)
    print(save_path4, 'saved')
    cv2.imwrite(save_path5, flip_image_5)
    print(save_path5, 'saved')
    cv2.imwrite(save_path6, flip_image_6)
    print(save_path6, 'saved')
    cv2.imwrite(save_path7, flip_image_7)
    print(save_path7, 'saved')

def save_flip_label(name, raw_label_path, label_save_dir):
    # class x_center y_center width height
    with open(raw_label_path) as raw_label:
        out_label_path = os.path.join(label_save_dir, name + "_flip1.txt")
        with open(out_label_path, "w") as out_label:
            for line in raw_label.readlines():
                words = line.split(" ")
                out_label.write(
                    words[0] + " " + words[1] + " " +
                    format(1 - float(words[2]), ".6f") + " " +
                    words[3] + " " + words[4]
                )
            print(out_label.name, 'saved')

        raw_label.seek(0)
        out_label_path = os.path.join(label_save_dir, name + "_flip2.txt")
        with open(out_label_path, "w") as out_label2:
            for line in raw_label.readlines():
                words = line.split(" ")
                out_label2.write(
                    words[0] + " " +
                    format(1 - float(words[1]), ".6f") + " " +
                    words[2] + " " + words[3] + " " + words[4]
                )
            print(out_label.name, 'saved')

        raw_label.seek(0)
        out_label_path = os.path.join(label_save_dir, name + "_flip3.txt")
        with open(out_label_path, "w") as out_label:
            for line in raw_label.readlines():
                words = line.split(" ")
                out_label.write(
                    words[0] + " " +
                    format(1 - float(words[1]), ".6f") + " " +
                    format(1 - float(words[2]), ".6f") + " " +
                    words[3] + " " + words[4]
                )
            print(out_label.name, 'saved')

        raw_label.seek(0)
        out_label_path = os.path.join(label_save_dir, name + "_flip4.txt")
        with open(out_label_path, "w") as out_label:
            for line in raw_label.readlines():
                words = line.split(" ")
                out_label.write(
                    words[0] + " " +
                    format(1 - float(words[2]), ".6f") + " " +
                    words[1] + " " + words[4].strip('\n') + " " + words[3] + '\n'
                )
            print(out_label.name, 'saved')

    raw_label_path = os.path.join(label_save_dir, name + "_flip4.txt")
    with open(raw_label_path, "r") as raw_label:
        out_label_path = os.path.join(label_save_dir, name + "_flip5.txt")
        with open(out_label_path, "w") as out_label:
            for line in raw_label.readlines():
                words = line.split(" ")
                out_label.write(
                    words[0] + " " + words[1] + " " +
                    format(1 - float(words[2]), ".6f") + " " +
                    words[3] + " " + words[4]
                )
            print(out_label.name, 'saved')

        raw_label.seek(0)
        out_label_path = os.path.join(label_save_dir, name + "_flip6.txt")
        with open(out_label_path, "w") as out_label:
            for line in raw_label.readlines():
                words = line.split(" ")
                out_label.write(
                    words[0] + " " +
                    format(1 - float(words[1]), ".6f") + " " +
                    words[2] + " " + words[3] + " " + words[4]
                )
            print(out_label.name, 'saved')

        raw_label.seek(0)
        out_label_path = os.path.join(label_save_dir, name + "_flip7.txt")
        with open(out_label_path, "w") as out_label:
            for line in raw_label.readlines():
                words = line.split(" ")
                out_label.write(
                    words[0] + " " +
                    format(1 - float(words[1]), ".6f") + " " +
                    format(1 - float(words[2]), ".6f") + " " +
                    words[3] + " " + words[4]
                )
            print(out_label.name, 'saved')
