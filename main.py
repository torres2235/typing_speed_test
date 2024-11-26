from tkinter import *
import pandas as pd
import random
import time

window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=50)

canvas = Canvas(window, width=1000, height=200)

# replace with pandas eventually #
paragraphs = []
with open("data/paragraphs.txt", "r") as data:
    for line in data:
        paragraphs.append(line)
# ------------------------------ #
curr_paragraph = paragraphs[random.randint(0, len(paragraphs)-1)]
print(curr_paragraph)
full_paragraph = []
t = Text(window, fg='#808080', font=("Ariel", 25,), width=50, height=10)
t.insert(INSERT, curr_paragraph)
t.config(state=DISABLED)
# for i in range(len(curr_paragraph)):
#     #print(char)
#     text = Label(canvas, text=curr_paragraph[i], fg='#808080', font=("Ariel", 25,), wraplength=800, justify="center")
#     full_paragraph.append(text)
#     text.pack(side='left')
t.grid(row=0, column=0)


#print(full_paragraph[0])

user_input = Text(width=100,
                  height=5,
                  padx=10,
                  pady=10
                  )
user_input.grid(row=1, column=0)

def new_para():
    curr_paragraph = paragraphs[random.randint(0, len(paragraphs) - 1)]
    t.config(state=NORMAL)
    t.delete("1.0", END)
    t.insert(INSERT, curr_paragraph)
    t.config(state=DISABLED)
    print("displaying new paragraph")
    print(curr_paragraph)

next_btn = Button(
    text="New Paragraph",
    command=new_para
                  )
next_btn.grid(row=3, column=0)

#print(text['text'][0])
#t[0].config(fg='blue')

window.mainloop()
