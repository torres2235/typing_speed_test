from tkinter import *
from tkinter import font
import pandas as pd
import random
import math
from pynput import keyboard

curr_paragraph = None
timer = None
mistakes = 0
mistake_index = []


# ----------------  Functions  ----------------#
def new_para():
    global timer
    global curr_paragraph
    global mistakes
    mistakes = 0
    mistake_count.config(text="Mistakes: 0")
    curr_paragraph = paragraphs[random.randint(0, len(paragraphs) - 1)]
    display_text.config(state=NORMAL)
    display_text.delete("1.0", END)
    display_text.insert(INSERT, curr_paragraph)
    display_text.config(state=DISABLED)
    user_input.delete("1.0", END)
    print("displaying new paragraph")
    print(curr_paragraph)
    if timer:
        window.after_cancel(timer)
    start()


def start():
    timer_text.config(text="00:00")
    count_timer(00)
    change_color()
    calc_wpm(00)


def count_timer(time):
    global timer
    min = math.floor(time / 60)
    sec = time % 60
    if min < 10:
        min = "0" + str(min)
    if sec < 10:
        sec = "0" + str(sec)

    timer_text.config(text=f"{min}:{sec}")
    timer = window.after(1000, count_timer, time + 1)


def change_color():
    global mistakes
    global mistake_index
    display_font = font.Font(display_text, display_text.cget("font"))
    display_text.tag_config("red", font=display_font, foreground="Red")
    display_text.tag_config("green", font=display_font, foreground="Green")
    display_text.tag_config("grey_bg", font=display_font, background="lightgrey")

    dis = display_text.get(1.0, "end")
    usr = user_input.get(1.0, "end")

    for i in range(len(usr)-1):
        display_text.tag_remove("grey_bg", f"1.{i}")
        if usr[i] != dis[i]:
            if mistake_index.count(i) < 1:
                mistake_index.append(i)
                mistakes += 1
                mistake_count.config(text=f"Mistakes: {mistakes}")
            display_text.tag_add("red", f"1.{i}")
        else:
            display_text.tag_add("green", f"1.{i}")

    for tag in display_text.tag_names():
        display_text.tag_remove(tag, f"1.{len(usr)-1}", "end")

    display_text.tag_add("grey_bg", f"1.{len(usr)-1}")

    window.after(1, change_color)  # refresh


def calc_wpm(time):
    # wpm = (chars / 5) / mins
    if time > 0:
        usr = user_input.get(1.0, "end")
        wpm = round((len(usr) / 5) / (time/60), 2)
        wpm_count.config(text=f"WPM:{wpm}")

    window.after(1000, calc_wpm, time + 1)

# ----------------  Window  ----------------#
window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=50)

# replace with pandas eventually #
paragraphs = []
with open("data/paragraphs.txt", "r") as data:
    for line in data:
        paragraphs.append(line)
# ------------------------------ #

wpm_count = Label(text="WPM:0.0", fg="white", font=("Arial", 35, "bold"))
wpm_count.grid(row=0, column=0)
timer_text = Label(text="00:00", fg="white", font=("Arial", 35, "bold"))
timer_text.grid(column=1, row=0)
mistake_count = Label(text="Mistakes:0", fg="white", font=("Arial", 35, "bold"))
mistake_count.grid(row=0, column=2)

curr_paragraph = paragraphs[random.randint(0, len(paragraphs) - 1)]
print(curr_paragraph)
full_paragraph = []
display_text = Text(window,
                    fg='#808080',
                    font=("Ariel", 25,),
                    width=50,
                    height=10,
                    wrap=WORD,  # wrap at word boundary
                    )
display_text.insert(INSERT, curr_paragraph)
display_text.config(state=DISABLED)
display_text.grid(row=1, column=1)

user_input = Text(width=100,
                  height=5,
                  padx=10,
                  pady=10,
                  wrap=WORD,
                  )
user_input.grid(row=2, column=1)

next_btn = Button(text="New Paragraph", command=new_para)
next_btn.grid(row=3, column=1)

window.mainloop()
