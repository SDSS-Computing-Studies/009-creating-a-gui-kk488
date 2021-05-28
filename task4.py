import tkinter as tk
from tkinter import *

window=tk.Tk()

window.title("example")
window.geometry("290x130")
dogphoto=PhotoImage(file="dog.png")
label1=tk.Label(window, image=dogphoto)
label2=tk.Label(window, text="pochacco!")
label3=tk.Label(window, text="A cuddly little puppy! This is form the same\ncreators who brought you Keropi and Kero Kero",bg="#A3FFFF")

label1.place(x=90,y=0)
label2.place(x=150,y=50)
label3.place(x=0,y=90)
window.mainloop()