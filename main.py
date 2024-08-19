from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=50)


user_input = StringVar()
input_entry = ttk.Entry(width=21)
input_entry.grid(column=1, row=1)

window.mainloop()
