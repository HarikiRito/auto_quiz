import time
from typing import List

from google import google
import PIL
from PIL import Image
import PIL.ImageOps
from google.modules.standard_search import GoogleResult


class PilUtils:
    @staticmethod
    def scale(img: Image, ws: float = 1, hs: float = 1) -> Image:
        width, height = img.size
        size = int(width * ws), int(height * hs)
        return img.resize(size, Image.ANTIALIAS)

    @staticmethod
    def custom_scale(img: Image, width=1191, height=2000) -> Image:
        return img.resize((width, height), Image.ANTIALIAS)

    @staticmethod
    def change_contrast(img: Image, level: int = 0) -> Image:
        factor = (259 * (level + 255)) / (255 * (259 - level))

        def contrast(c):
            return 128 + factor * (c - 128)

        return img.point(contrast)

    @staticmethod
    def invert(img: Image):
        return PIL.ImageOps.invert(img)


class TP:
    @staticmethod
    def split(text: str):
        q, a = text.split('?')
        list_item = [TP.clean_text(item) for item in
                     a.split('\n') if len(item) > 0]
        list_item = [TP.clean_text(q)] + list_item

        if len(list_item) > 4:
            list_item = list_item[-4:]
        return list_item

    @staticmethod
    def clean_text(item: str):
        print(item)
        item = item.replace('\n', ' ')
        item = item.replace('\'', '')
        item = item.replace('\\', '')
        item = item.replace('/', '')
        item = item.replace('_', '')
        item = item.replace(' ⁄', '')
        item = item.replace('.', '')
        item = item.replace('—', '')
        item = item.replace('<', '')
        item = item.replace('=', '')
        return item

    @staticmethod
    def is_useless(text: str):
        ignore = ['Chơi cho vui', 'Câu hỏi', 'TRỰC TIẾP', 'of', 'Question']
        return not any(x in text for x in ignore)


class GoogleSearch:
    result: List[GoogleResult] = None

    def __init__(self, q: str, num: int = 2):
        self.q = q
        self.num = num

    def search(self, num: int = 1):
        self.result = google.search(self.q, self.num)


def calculate_time(func):
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):
        # storing time before function execution
        begin = time.time()

        res = func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)
        return res

    return inner1
