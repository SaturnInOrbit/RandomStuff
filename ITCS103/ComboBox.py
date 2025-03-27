import tkinter as tk
from tkinter import ttk

def select(event):
    selected_item = combo_box.get()
    label.config(text="Selected Item: " + selected_item)

window = tk.Tk()
window.geometry('300x300')

label = tk.Label(window, text="Selected Item: ")
label.pack(pady=10)

combo_box = ttk.Combobox(window, values=['Option 1', 'Option 2', 'Option 3'])
combo_box.pack(pady=5)

combo_box.set("Option 1")

combo_box.bind("<<ComboboxSelected>>", select)

window.mainloop()
