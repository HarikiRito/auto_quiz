import os
from tkinter import *
import numpy as np
import pyautogui
import imutils
import cv2

from text_extract.clould_vision import detect_text
from text_extract.pil_utils import calculate_time, TextProcessor


class BuilderUI:
    def __init__(self, tk: Tk):
        self.tk = tk
        self.x1 = self.make_entry()
        self.y1 = self.make_entry()
        self.x2 = self.make_entry()
        self.y2 = self.make_entry()

    def make_entry(self, width=5, **options):
        entry = Entry(self.tk, **options)
        if width:
            entry.config(width=width)
        return entry

    def input_cor(self):
        Label(self.tk, text='x1').grid(row=0, column=0)
        Label(self.tk, text='y1').grid(row=0, column=2)
        Label(self.tk, text='x2').grid(row=1, column=0)
        Label(self.tk, text='y2').grid(row=1, column=2)

        self.x1.insert(END, '0')
        self.y1.insert(END, '0')
        self.x2.insert(END, '500')
        self.y2.insert(END, '500')

        self.x1.grid(row=0, column=1)
        self.y1.grid(row=0, column=3)
        self.x2.grid(row=1, column=1)
        self.y2.grid(row=1, column=3)

    def set_coord(self):
        b = Button(self.tk, text='Set', command=self.confirm_set_coord)
        b.config(width=5)
        b.grid(row=2, column=1)

    @calculate_time
    def confirm_set_coord(self):
        x1 = int(self.x1.get())
        y1 = int(self.y1.get())
        x2 = int(self.x2.get())
        y2 = int(self.y2.get())
        if x2 <= x1:
            x2 = x1 + 300
        if y2 <= y1:
            y2 = y1 + 300

        a = [x1, y1]
        b = [x2, y2]
        c = list(np.subtract(b, a))
        region = a + c
        image = pyautogui.screenshot(region=region)
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        cv2.imwrite("test.png", image)
        abs_path = os.path.abspath('test.jpg')
        text = detect_text(abs_path)
        result = self.split_text_vision(text)
        print(result)

    def split_text_vision(self, text: str):
        q: str = ''
        q, a = text.split('?')
        question = q.replace('\n', ' ') + '?'
        answers = [item for item in a.split('\n') if item]

        return [question, answers]
