from tkinter import *
from random import choice
import csv
import json
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
LENG_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, 'bold')

# --------------- MANAGE DATA FROM CSV

open_file = pd.read_csv("./data/french_words.csv")
df = open_file.to_dict(orient="records")    # Parameter orient changed to "records"
print(df)


def next_card():
    current_card = choice(df)
    front_canvas.itemconfig(card_title, text='French')
    front_canvas.itemconfig(card_word, text=current_card["French"])

# --------------- User Interface Tkinter


window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title('Flash Card Translator Game')
window.minsize(width=800, height=525)

# Importing images fro Buttons
check_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")

# Buttons
check_button = Button(image=check_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
check_button.grid(column=1, row=1)
cross_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
cross_button.grid(column=0, row=1)

# CANVAS
front_canvas = Canvas(width=800, height=526)
front_card = PhotoImage(file="./images/card_front.png")
front_canvas.create_image(400, 263, image=front_card)
card_title = front_canvas.create_text(400, 150, text=f"French", font=LENG_FONT)
card_word = front_canvas.create_text(400, 263, text=f"", font=WORD_FONT)
front_canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
front_canvas.grid(column=0, row=0, columnspan=2)

next_card()

window.mainloop()
