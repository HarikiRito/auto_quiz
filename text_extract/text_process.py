import os

import cv2
from dotenv import load_dotenv
from datetime import datetime
from PIL import Image, ImageFilter
from pytesseract import image_to_string
import glob
import time

from text_extract.pil_utils import PilUtils, TextProcessor
from text_extract.tesseract import Tesseract, TesseractOpenCV

load_dotenv()
paths = ['../images/*.jpg', '../images/*.png']
list_file = []
for path in paths:
    list_file.extend(glob.glob(path))

# for path in list_file:
#     img = Tesseract(path)
#     text = img.get_text()
#     print(TextProcessor.split(text))

for path in list_file:
    img = TesseractOpenCV(path)
    img.process()
    text = img.get_text()
    print(TextProcessor.split(text))

img = TesseractOpenCV(list_file[8])
img.process()
text = img.get_text()
print(TextProcessor.split(text))
cv2.imwrite('test.png', img.image)
