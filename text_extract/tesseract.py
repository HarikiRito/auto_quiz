import asyncio

from PIL import Image, ImageFilter
from pytesseract import image_to_string

from text_extract.pil_utils import calculate_time


class Tesseract:
    def __init__(self, path: str):
        self.image = Image.open(path).convert('LA')

    @calculate_time
    def get_text(self) -> str:
        # img = PilUtils.change_contrast(img, 100)
        img = self.image.filter(ImageFilter.SMOOTH_MORE)
        text = image_to_string(img, lang='vie')
        return text
