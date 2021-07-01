from tkinter import *
from random import choice
import pandas as pd
import time

BACKGROUND_COLOR = "#B1DDC6"
LENG_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, 'bold')
current_card = {}
to_learn = {}

# --------------- MANAGE DATA FROM CSV
try:
    to_learn = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    open_file = pd.read_csv("./data/french_words.csv")
    to_learn = open_file.to_dict(orient="records")    # Parameter orient changed to "records"
else:
    to_learn = to_learn.to_dict(orient="records")
# print(df)


def next_card():
    global current_card
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_card, image=front_card)
    window.after(3000, func=flip_card)

# --------------- FLIP THE CARDS


def flip_card():
    """Flips the card when the check button is clicked to reveal the English word."""
    canvas.itemconfig(canvas_card, image=back_card)
    canvas.itemconfig(card_title, text=f"English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# -------------- REMOVING KNOWN CARDS


def is_know():
    """Removes the cards that are in the list of words to learn"""
    to_learn.remove(current_card)
    next_card()



# --------------- User Interface Tkinter


window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title('Flash Card Translator Game')
window.minsize(width=800, height=525)
# flip_timer = window.after(3000)

# Importing images fro Buttons
check_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")

# Buttons
check_button = Button(image=check_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
check_button.grid(column=1, row=1)
cross_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_know)
cross_button.grid(column=0, row=1)

# CANVAS
canvas = Canvas(width=800, height=526)
front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")
canvas_card = canvas.create_image(400, 263, image=front_card)
card_title = canvas.create_text(400, 150, text=f"French", font=LENG_FONT)
card_word = canvas.create_text(400, 263, text=f"", font=WORD_FONT)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

next_card()

window.mainloop()
