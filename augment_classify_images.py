from PIL import Image
import albumentations as A
import os
import numpy as np


class augment_classify_images:
    def annotate_from_list(self, list_of_images, transform_list):
        for image_path in list_of_images:
            pillow_image = Image.open(image_path)
            image = np.array(pillow_image)
            for idx, transform in enumerate(transform_list):
                transformed_image = transform(image=image)['image']
                print(image_path)
                base_name, extension = os.path.splitext(image_path)
                transformed_image = Image.fromarray(transformed_image)
                transformed_image.save(f"{base_name}_{idx}{extension}")

    def __init__(self):
        self.flip_transform = A.Compose([
            A.HorizontalFlip(p=0.5)
        ])
        self.brightness_transform = A.Compose([
            A.RandomBrightnessContrast(p=0.2),
        ])
        self.rotate_transform = A.Compose([
            A.RandomRotate90(p=0.5),
        ])
        self.rgb_shift_transform = A.Compose([
            A.RGBShift(p=0.5),
        ])
        self.rotate_augmentation = A.Compose([
            A.Rotate(p=0.5),
        ])

        self.path = input('Enter path of images: ')
        self.all_images = os.listdir(os.path.abspath(self.path))
        self.all_images = [os.path.abspath(os.path.join(self.path, i)) for i in self.all_images]
        self.transform_list = [
            self.flip_transform,
            self.brightness_transform,
            self.rotate_transform,
            self.rgb_shift_transform,
            self.rotate_augmentation
        ]

        self.annotate_from_list(self.all_images, self.transform_list)


augment_classify_images()
