import PIL
from PIL import Image
import PIL.ImageOps


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


class TextProcessor:
    @staticmethod
    def split(text: str):
        list_item = [item.replace('\n', ' ') for item in
                     text.split('\n\n') if TextProcessor.is_useless(item)]
        return list_item

    @staticmethod
    def is_useless(text: str):
        ignore = ['Chơi cho vui', 'Câu hỏi']
        return not any(x in text for x in ignore)
