from tkinter import *

BG_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BG_COLOR)
window.resizable(False, False)
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BG_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))

canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0)
known_button.grid(column=1, row=1)


window.mainloop()
