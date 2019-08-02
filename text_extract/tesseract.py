import asyncio

from PIL import Image, ImageFilter
from pytesseract import image_to_string

from text_extract.pil_utils import calculate_time, PilUtils


class Tesseract:
    def __init__(self, path: str):
        self.image = Image.open(path).convert('LA')

    @calculate_time
    def get_text(self) -> str:
        self.image = PilUtils.change_contrast(self.image, 12)
        self.image = self.image.filter(ImageFilter.SMOOTH_MORE)
        text = image_to_string(self.image, lang='vie')
        return text
