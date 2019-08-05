from tkinter import *
from tkinter import messagebox
import numpy as np
import pyautogui
import imutils
import cv2
from dotenv import load_dotenv

from gui.input_grid import BuilderUI

app = Tk()
load_dotenv()

app.geometry('500x500')
builder = BuilderUI(app)

builder.input_cor()
builder.set_coord()

app.mainloop()
