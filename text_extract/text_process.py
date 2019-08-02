import os

from dotenv import load_dotenv
from PIL import Image, ImageFilter
from pytesseract import image_to_string
import glob
import time

from text_extract.pil_utils import PilUtils, TextProcessor
from text_extract.tesseract import Tesseract

load_dotenv()

list_file = glob.glob("../images/*.jpg")
for path in list_file:
    img = Tesseract(path)
    text = img.get_text()
    print(TextProcessor.split(text))
