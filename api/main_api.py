import os
from datetime import datetime

import cv2
import numpy as np
import pyautogui
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask_cors import CORS

from api.seach import google_search_get
from text_extract.clould_vision import detect_text
from text_extract.pil_utils import TP
from text_extract.tesseract import TesseractOpenCV
from text_extract.text_utils import TextU

app = FlaskAPI(__name__)
CORS(app)

notes = {
    0: 'do the shopping',
    1: 'build the codez',
    2: 'paint the door',
}


def calculate_region(x1, y1, x2, y2):
    if x2 <= x1:
        x2 = x1 + 300
    if y2 <= y1:
        y2 = y1 + 300
    a = [x1, y1]
    b = [x2, y2]
    c = list(np.subtract(b, a))
    region = a + c
    return region


@app.route("/text", methods=['GET', 'POST'])
def notes_list():
    """
    List or create notes.
    """
    if request.method == 'POST':
        x1: str = request.data.get('x1')
        y1: str = request.data.get('y1')
        x2: str = request.data.get('x2')
        y2: str = request.data.get('y2')
        region = calculate_region(x1, y1, x2, y2)
        image = pyautogui.screenshot(region=region)
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        # image = cv2.imread('gui/2019-08-22_21-31-19.png')
        file_name = 'gui/{}.png'.format(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
        # cv2.imwrite(file_name, image)
        abs_path = os.path.abspath('gui/2019-08-23_21-28-30.png')
        # text = detect_text(abs_path)
        # result = TextU.split_from_vision(text)

        img = TesseractOpenCV(abs_path)
        img.process()
        text = img.get_text()
        # print(text)
        result = TP.split(text)
        return {
            'question': result[0],
            'answers': [item for item in result][1:],
            'text': text
        }

    # request.method == 'GET'


if __name__ == "__main__":
    app.run(port=8888, debug=True, passthrough_errors=True)
