import os
import cv2

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image at path {image_path} could not be loaded.")

    image = cv2.resize(image, (256, 256))

    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    return image