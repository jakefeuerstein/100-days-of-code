from tkinter import *
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"



#---------Create Flash Card---------------

#Read Data

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
finally:
    dict = df.to_dict(orient="records")
    current_card = {}


#Next French Card

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(dict)
    card_canvas.itemconfig(card_image, image=card_front_image)
    card_canvas.itemconfig(card_title, text="French", fill="black")
    card_canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, english_card)

# Show English Card

def english_card():
    card_canvas.itemconfig(card_image, image=card_back_image)
    card_canvas.itemconfig(card_title, text="English", fill="white")
    card_canvas.itemconfig(card_word, text=current_card["English"], fill="white")

# Card Known

def card_known():
    dict.remove(current_card)
    df = pd.DataFrame.from_dict(dict)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()

#---------UI---------------

#Window

window = Tk()
window.title("Flashy")
window.config(width=1000, height=700, padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, english_card)

#Card Canvas

card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_image = card_canvas.create_image(400, 263, image=card_front_image)
card_title = card_canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), tag="canvas_title")
card_word = card_canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), tag="canvas_word")
card_canvas.grid(row=0, column=0, columnspan=2)

card_back_image = PhotoImage(file="images/card_back.png")
# card_back = card_canvas.create_image(800, 526, image=card_front_image)

#Buttons

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=card_known)
right_button.grid(row=1, column=0)

wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=1)

next_card()

print(dict)

window.mainloop()