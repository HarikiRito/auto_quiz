from tkinter import *
from tkinter import messagebox
import numpy as np
import pyautogui
import imutils
import cv2

from gui.input_grid import BuilderUI

app = Tk()

app.geometry('500x500')
buider = BuilderUI(app)

buider.input_cor()


def helloCallBack():
    a = [376, 135]
    b = [590, 368]
    c = list(np.subtract(b, a))
    region = a + c
    image = pyautogui.screenshot(region=region)
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite("test.png", image)


e1 = Entry(app)
e2 = Entry(app)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

app.mainloop()
