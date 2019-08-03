import asyncio

from PIL import Image, ImageFilter
from pytesseract import image_to_string

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

