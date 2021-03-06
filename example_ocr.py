import pytesseract as tess
tess.pytesseract.tesseract_cmd=r'C:\Users\Archit\AppData\Local\Tesseract-OCR\tesseract.exe'
from pytesseract import image_to_string
import cv2
import numpy as np
try:
    from PIL import Image
except ImportError:
    import Image



def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """

    image = np.float32(Image.open(filename))
    img = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones ((1, 1), np.uint8)
    img = cv2.dilate (img, kernel, iterations=1)
    img = cv2.erode (img, kernel, iterations=1)

    text = image_to_string(img)  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

