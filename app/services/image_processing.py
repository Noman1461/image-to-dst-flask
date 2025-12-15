import cv2
import numpy as np

def preprocess_image(image_path):
    """
    Loads image, converts to binary, returns processed image.
    """
    img = cv2.imread(image_path)

    if img is None:
        raise ValueError("Image could not be loaded")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Binary threshold
    _, binary = cv2.threshold(
        blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    return binary
