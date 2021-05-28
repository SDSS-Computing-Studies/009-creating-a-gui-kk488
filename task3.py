import tkinter as tk
from tkinter import *

window=tk.Tk()

window.title("example")
dogphoto=PhotoImage(file="dog.png")
label1=tk.Label(window, image=dogphoto)
label2=tk.Label(window, text="pochacco!")
label3=tk.Label(window, text="A cuddly little puppy! This is form the same\ncreators who brought you Keropi and Kero Kero",bg="#A3FFFF")

label1.grid(row=1,column=2,rowspan=3,columnspan=2)
label2.grid(row=2,column=3,columnspan=2)
label3.grid(row=4,column=2,columnspan=3)

window.mainloop()