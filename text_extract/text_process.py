import os

from dotenv import load_dotenv
from PIL import Image, ImageFilter
from pytesseract import image_to_string
import glob
import time

from text_extract.pil_utils import PilUtils, TextProcessor

load_dotenv()

start = time.time()
print(os.environ)
list_file = glob.glob("../images/*.jpg")
img: Image = Image.open(list_file[2]).convert('LA')
# img = PilUtils.change_contrast(img, 100)
img = img.filter(ImageFilter.SMOOTH_MORE)
text = image_to_string(img, lang='vie')
end = time.time()
print(text)
print(TextProcessor.split(text))
print(end - start)

img.save('test.png')
