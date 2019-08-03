import asyncio

import cv2
import imutils
from PIL import Image, ImageFilter
from pytesseract import image_to_string
import numpy as np

from text_extract.pil_utils import calculate_time, PilUtils


class Tesseract:
    def __init__(self, path: str):
        self.image = Image.open(path).convert('LA')

    @calculate_time
    def get_text(self, contrast: int = 12, filter_type: ImageFilter = ImageFilter.SMOOTH_MORE) -> str:
        self.image = PilUtils.change_contrast(self.image, contrast)
        self.image = self.image.filter(filter_type)
        text = image_to_string(self.image, lang='vie')
        return text


class TesseractOpenCV:
    def __init__(self, path: str):
        self.image = cv2.imread(path)

    def get_text(self, color=cv2.COLOR_BGR2GRAY):
        # self.image = cv2.bitwise_not(self.image)
        self.image = cv2.cvtColor(self.image, color)
        # self.scale()
        # self.simple_thresholding()
        self.remove_noise_and_smooth()
        self.apply_brightness_contrast(contrast=2)
        text = image_to_string(self.image, lang='vie')
        return text

    def scale(self):
        scale_percent = 60  # percent of original size
        width = int(self.image.shape[1] * scale_percent / 100)
        height = int(self.image.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        self.image = cv2.resize(self.image, dim, interpolation=cv2.INTER_AREA)

    def simple_thresholding(self):
        th3 = cv2.adaptiveThreshold(self.image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                                    cv2.THRESH_BINARY, 11, 2)

        self.image = th3

    def remove_noise_and_smooth(self):
        img = self.image
        filtered = cv2.adaptiveThreshold(img.astype(np.uint8), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9,
                                         30)
        kernel = np.ones((1, 1), np.uint8)
        opening = cv2.morphologyEx(filtered, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
        or_image = cv2.bitwise_or(img, closing)
        self.image = or_image

    def apply_brightness_contrast(self, brightness=0, contrast=0):

        if brightness != 0:
            if brightness > 0:
                shadow = brightness
                highlight = 255
            else:
                shadow = 0
                highlight = 255 + brightness
            alpha_b = (highlight - shadow) / 255
            gamma_b = shadow

            buf = cv2.addWeighted(self.image, alpha_b, self.image, 0, gamma_b)
        else:
            buf = self.image.copy()

        if contrast != 0:
            f = 131 * (contrast + 127) / (127 * (131 - contrast))
            alpha_c = f
            gamma_c = 127 * (1 - f)

            buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

        self.image = buf
