import random
import pandas
from tkinter import *

BG_COLOR = "#B1DDC6"

random_card = {}
to_learn = {}

# -------------------------- READING DATA ----------------------------- #

try:
    read_file = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    read_file = pandas.read_csv("data/french_words.csv")
    to_learn = read_file.to_dict("records")

else:
    to_learn = pandas.DataFrame(read_file).to_dict("records")


def next_card():
    global random_card, timer
    window.after_cancel(timer)
    random_card = random.choice(to_learn)
    canvas.itemconfig(card_bg, image=card_front_img)
    canvas.itemconfig(canvas_title, text="FRENCH", fill="black")
    canvas.itemconfig(canvas_word, text=random_card["French"].capitalize(), fill="black")
    timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_bg, image=card_back_img)
    canvas.itemconfig(canvas_title, text="ENGLISH", fill="white")
    canvas.itemconfig(canvas_word, text=random_card["English"].capitalize(), fill="white")


def is_known():
    to_learn.remove(random_card)
    print(len(to_learn))
    pandas.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)

    next_card()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BG_COLOR)
timer = window.after(3000, func=lambda: flip_card())

window.resizable(False, False)
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BG_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

canvas_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))

canvas_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()
