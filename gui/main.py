from tkinter import *
from tkinter import messagebox

top = Tk()


def helloCallBack():
    messagebox.showinfo("Hello Python", "Hello World")


B = Button(top, text="Hello", command=helloCallBack)
C = Button(top, text="Hello 2", command=helloCallBack)
top.mainloop()
