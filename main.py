from tkinter import *
#from tkinter import ttk
import pandas as pd
import random

window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=50)

canvas = Canvas(width=350, height=200)
with open("data/paragraphs.txt", "r") as data:
    paragraphs = []
    for line in data:
        paragraphs.append(line)
    canvas.create_text(175, 100, text=paragraphs[random.randint(0, len(paragraphs))], font=("Ariel", 20))
    canvas.pack()
canvas.grid(row=0, column=0)

text = Text(width=50,
            height=5,
            padx=10,
            pady=10
            )
text.grid(row=1, column=0)

window.mainloop()
