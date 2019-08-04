from tkinter import *


class BuilderUI:
    def __init__(self, tk: Tk):
        self.tk = tk

    def input_cor(self):
        Label(self.tk, text='x1').grid(row=0, column=0)
        Label(self.tk, text='y1').grid(row=0, column=2)
        Label(self.tk, text='x2').grid(row=1, column=0)
        Label(self.tk, text='y2').grid(row=1, column=2)

        x1 = Entry(self.tk)
        y1 = Entry(self.tk)
        x2 = Entry(self.tk)
        y2 = Entry(self.tk)

        x1.grid(row=0, column=1)
        y1.grid(row=0, column=3)
        x2.grid(row=1, column=1)
        y2.grid(row=1, column=3)
