from tkinter import *
import pandas as pd
import random
import time

window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=50)

# replace with pandas eventually #
paragraphs = []
with open("data/paragraphs.txt", "r") as data:
    for line in data:
        paragraphs.append(line)
# ------------------------------ #
text = Label(text=paragraphs[random.randint(0, len(paragraphs))], font=("Ariel", 25), wraplength=800, justify="center")
text.grid(row=0, column=0)

text = Text(width=50,
            height=5,
            padx=10,
            pady=10
            )
text.grid(row=1, column=0)

window.mainloop()
