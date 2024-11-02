from tkinter import *
from tkinter import messagebox
import pandas
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
random_item = None

try:
    data = pandas.read_csv(filepath_or_buffer="./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv(filepath_or_buffer="./data/french_words.csv")
else:
    pass
finally:
    to_learn = data.to_dict(orient="records")
#------------------------- KNOWN WORDS FUNCTION -------------------------#
def is_known():
    to_learn.remove(random_item)
    df = pandas.DataFrame(to_learn)
    df.to_csv("./data/words_to_learn.csv", index=False)
    if len(to_learn)!=0:
        next_card()
    else:
        messagebox.showinfo(title="Information", message="Thats All :) You Finished all the cards")
        os.remove("./data/words_to_learn.csv")
#-------------------------- FLIP CARD FUNCTION --------------------------#
def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=random_item["English"], fill="white")
    canvas.itemconfig(card_image, image=back_card_image)

#-------------------------- NEXT CARD FUNCTION --------------------------#
def next_card():
    global random_item, flip_timer
    window.after_cancel(flip_timer)
    random_item = random.choice(to_learn)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=random_item["French"], fill="black")
    canvas.itemconfig(card_image, image=front_card_image)
    flip_timer = window.after(3000, flip_card)

#------------------------------- UI SETUP -------------------------------#
window = Tk()
window.title("Flash Card")
window.resizable()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)
#-------------------------------------------------------------------------
# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
back_card_image = PhotoImage(file="./images/card_back.png")
front_card_image = PhotoImage(file="./images/card_front.png")
card_image = canvas.create_image(400, 263, image=front_card_image)
title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#-------------------------------------------------------------------------
# Buutons
cross_image = PhotoImage(file="./images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, border=False, command=next_card)
cross_button.grid(column=0, row=1)

check_image = PhotoImage(file="./images/right.png")
check_button = Button(image=check_image, highlightthickness=0, border=False, command=is_known)
check_button.grid(column=1 , row=1)

next_card()

# Main Loop
window.mainloop()