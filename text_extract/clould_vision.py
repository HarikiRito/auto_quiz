import io
import os

from dotenv import load_dotenv

# Imports the Google Cloud client library
import cv2
from google.cloud import vision
from google.cloud.vision import types

load_dotenv()


# Instantiates a client
def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    all_text = '{}'.format(texts[0].description)
    return all_text
