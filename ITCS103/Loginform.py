from cProfile import label
import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x300")

label = tk.Label(text="Login", fg="blue", font="Arial 15")
label.pack(padx=2, pady=2)

entry = tk.Entry(font= "Arial 10", width= 20)
entry.insert(index=2, string="Username")
entry.pack(padx=2,pady=2)


window.mainloop()