import asyncio
import os
from datetime import datetime
from tkinter import *
import numpy as np
import pyautogui
import imutils
import cv2

from api.seach import search_all
from text_extract.clould_vision import detect_text
from text_extract.pil_utils import calculate_time, TextProcessor
from text_extract.text_utils import TextU


class BuilderUI:
    def __init__(self, tk: Tk):
        self.tk = tk
        self.x1 = self.make_entry()
        self.y1 = self.make_entry()
        self.x2 = self.make_entry()
        self.y2 = self.make_entry()
        self.enable_vision = IntVar()
        self.enable_parse = IntVar()
        self.enable_search = IntVar()
        self.enable_save_image = IntVar()
        self.result = None

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
        self.y1.insert(END, '480')
        self.x2.insert(END, '390')
        self.y2.insert(END, '710')

        self.x1.grid(row=0, column=1)
        self.y1.grid(row=0, column=3)
        self.x2.grid(row=1, column=1)
        self.y2.grid(row=1, column=3)

    def set_coord(self):
        b = Button(self.tk, text='Set', command=self.confirm_set_coord)
        b.config(width=5)
        b.grid(row=2, column=1)

        Checkbutton(self.tk, text='Enable Vision', variable=self.enable_vision).grid(row=2, column=5, sticky=W)
        Checkbutton(self.tk, text="Enable Parse", variable=self.enable_parse).grid(row=2, column=6, sticky=W)
        Checkbutton(self.tk, text="Enable Search", variable=self.enable_search).grid(row=2, column=7, sticky=W)
        Checkbutton(self.tk, text="Save Image", variable=self.enable_save_image).grid(row=3, column=5, sticky=W)

    @calculate_time
    def confirm_set_coord(self):
        region = self.calculate_region()
        image = pyautogui.screenshot(region=region)
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        file_name = '{}.png'.format(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))

        if self.enable_save_image.get():
            cv2.imwrite(file_name, image)
        abs_path = os.path.abspath('test.png')
        if self.enable_search.get():
            text = detect_text(abs_path)
            self.result = TextU.split_from_vision(text)
        print(self.result)
        q, answers = self.result
        search_result = asyncio.run(search_all(q, answers))
        print(search_result)

    def calculate_region(self):
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
        return region
