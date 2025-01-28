from tkinter import *
from tkinter import font
import pandas as pd
import random
import math

curr_paragraph = None
timer = None
wpm = None
overall_mistakes = 0
curr_mistakes = 0
mistake_index = []


# ----------------  Functions  ----------------#
def new_para():
    global curr_paragraph
    mistake_count.config(text="Mistakes: 0")
    curr_paragraph = paragraphs[random.randint(0, len(paragraphs) - 1)]
    display_text.config(state=NORMAL)
    display_text.delete("1.0", END)
    display_text.insert(INSERT, curr_paragraph)
    display_text.config(state=DISABLED)
    user_input.config(state=NORMAL)
    user_input.delete("1.0", END)
    print("displaying new paragraph")
    print(curr_paragraph)



def start():
    global timer
    global wpm
    global mistakes
    mistakes = 0
    start_btn.config(text="Reset")
    if timer:
        window.after_cancel(timer)
        window.after_cancel(wpm)
    new_para()
    count_timer(60)
    change_color()
    calc_wpm(00)
    calc_accuracy()


def count_timer(time):
    global timer
    min = math.floor(time / 60)
    sec = time % 60
    if min < 10:
        min = "0" + str(min)
    if sec < 10:
        sec = "0" + str(sec)

    timer_text.config(text=f"{min}:{sec}")
    timer = window.after(1000, count_timer, time - 1)

    if time < 1:
        window.after_cancel(timer)
        window.after_cancel(wpm)
        user_input.config(state=DISABLED)


def change_color():
    global overall_mistakes
    global curr_mistakes
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
                overall_mistakes += 1
                #curr_mistakes += 1
                mistake_count.config(text=f"Mistakes: {overall_mistakes}")
            display_text.tag_add("red", f"1.{i}")
        else:
            #if mistake_index.count(i) > 0:
                #curr_mistakes -= 1
            display_text.tag_add("green", f"1.{i}")

    for tag in display_text.tag_names():
        display_text.tag_remove(tag, f"1.{len(usr)-1}", "end")

    display_text.tag_add("grey_bg", f"1.{len(usr)-1}")

    self = window.after(1, change_color)  # refresh

    if len(usr) == len(dis)-1:
        window.after_cancel(timer)
        window.after_cancel(wpm)
        window.after_cancel(self)
        user_input.config(state=DISABLED)


def calc_wpm(time):
    global wpm
    global overall_mistakes
    if time > 0:
        usr = user_input.get(1.0, "end")
        word_count = (len(usr)-1)
        gross_wpm = (word_count / 5) #/ (time/60)
        net_wpm = ((gross_wpm - overall_mistakes) / (time/60)) if ((gross_wpm - overall_mistakes) / (time/60)) > 0 else 0
        wpm_count.config(text=f"WPM: {net_wpm:.2f}")

    wpm = window.after(1000, calc_wpm, time + 1)


def calc_accuracy():
    global overall_mistakes
    usr = user_input.get(1.0, "end")
    percentage = ((len(usr) - overall_mistakes) / len(usr)) * 100
    accuracy.config(text=f"Accuracy: {percentage:.2f}%")

    acc = window.after(1000, calc_accuracy)


# ----------------  Window  ----------------#
window = Tk()
window.title("Typing Speed Test")
window.config(padx=25, pady=15)

# replace with pandas eventually #
paragraphs = []
with open("data/paragraphs.txt", "r") as data:
    for line in data:
        paragraphs.append(line)
# ------------------------------ #

wpm_count = Label(text="WPM: 00.00", fg="white", font=("Arial", 30, "bold"))
wpm_count.grid(row=1, column=3)
timer_text = Label(text="00:00", fg="white", font=("Arial", 35, "bold"))
timer_text.grid(row=0,column=1)
mistake_count = Label(text="Mistakes: 0", fg="white", font=("Arial", 30, "bold"))
mistake_count.grid(row=2, column=3)
accuracy = Label(text="Accuracy: 00.00%", fg="white", font=("Arial", 30, "bold"))
accuracy.grid(row=3, column=3)

display_text = Text(window,
                    fg='#808080',
                    font=("Ariel", 25,),
                    width=40,
                    height=10,
                    padx=10,
                    pady=5,
                    wrap=WORD,  # wrap at word boundary
                    )
display_text.insert(INSERT, "Click 'start' to begin . . .")
display_text.config(state=DISABLED)
display_text.grid(row=1, column=0, rowspan=3, columnspan=3)

user_input = Text(width=91,
                  height=5,
                  padx=10,
                  pady=10,
                  wrap=WORD,
                  )
user_input.insert(INSERT, "Type here . . .")
user_input.grid(row=4, column=0, columnspan=3)

start_btn = Button(text="Start", font=("Ariel", 14, "bold"), height=2, command=start)
start_btn.grid(row=5, column=1)

window.mainloop()
