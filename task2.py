import tkinter as tk
from tkinter import *

window=tk.Tk()
window.title("T-Town Veterinary Clinic Database")

button1=tk.Button(window,text="search by name")
entry1=tk.Entry(window,text="searched name")
dogphoto=PhotoImage(file="dog.png")

label1=tk.Label(window,image=dogphoto)
label2=tk.Label(window,text="client database")
label3=tk.Label(window,text="name")
label4=tk.Label(window,text="type")
label5=tk.Label(window,text="breed")
label6=tk.Label(window,text="owner")
label7=tk.Label(window,text="birthdate")

entry2=tk.Entry(window,width=15)
entry3=tk.Entry(window,width=15)
entry4=tk.Entry(window,width=15)
entry5=tk.Entry(window,width=15)
entry6=tk.Entry(window,width=15)

button2=tk.Button(window,text="< previous")
button3=tk.Button(window,text="next >")
button4=tk.Button(window,text="save entry")

button1.grid(row=1,column=4)
entry1.grid(row=1,column=5)
label1.grid(row=1,column=1,rowspan=2)
label2.grid(row=2,column=3)
label3.grid(row=3,column=1)
label4.grid(row=3,column=2)
label5.grid(row=3,column=3)
label6.grid(row=3,column=4)
label7.grid(row=3,column=5)
entry2.grid(row=4,column=1)
entry3.grid(row=4,column=2)
entry4.grid(row=4,column=3)
entry5.grid(row=4,column=4)
entry6.grid(row=4,column=5)
button2.grid(row=5,column=1)
button3.grid(row=5,column=5)
button4.grid(row=5,column=3)

window.mainloop()