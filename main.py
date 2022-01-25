import random
import pandas
from tkinter import *

p = pandas

BG_COLOR = "#B1DDC6"
# -------------------------- READING DATA ----------------------------- #


def next_card():
    with open("data/french_words.csv", 'r', encoding='utf-8') as data_file:
        read_file = pandas.read_csv(data_file)

        # With DataFrame
        p_df = pandas.DataFrame(read_file).to_dict("records")
        random_from_dict = random.choice(p_df)
        canvas.itemconfig(canvas_title, text="FRENCH")
        canvas.itemconfig(canvas_word, text=random_from_dict["French"].capitalize())

        canvas.after(3000, func=flip_card)


def flip_card():
    print("flipped!")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BG_COLOR)
window.resizable(False, False)
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BG_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

canvas_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))

canvas_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()
