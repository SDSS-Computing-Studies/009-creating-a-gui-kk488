import tkinter as tk
from tkinter import *

window=tk.Tk()
window.title("tk")
window.geometry("500x50")

nF=Frame()

entry1=tk.Entry(nF,text="number1")
label1=tk.Label(nF,text="x",borderwidth=5)
entry2=tk.Entry(nF,text="number2")
Button1=tk.Button(nF,text="=")
entry3=tk.Entry(nF,text="answer")

nF.pack()
entry1.pack(side=LEFT)
label1.pack(side=LEFT)
entry2.pack(side=LEFT)
Button1.pack(side=LEFT)
entry3.pack(side=LEFT)

window.mainloop()