from tkinter import *
import pandas
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_dict = {}

# Base directory where your script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# File paths using os.path.join
DATA_PATH = os.path.join(BASE_DIR, "data", "words_to_learn.csv")
ORIGINAL_DATA_PATH = os.path.join(BASE_DIR, "data", "french_words.csv")
CARD_FRONT_PATH = os.path.join(BASE_DIR, "images", "card_front.png")
CARD_BACK_PATH = os.path.join(BASE_DIR, "images", "card_back.png")
WRONG_IMG_PATH = os.path.join(BASE_DIR, "images", "wrong.png")
RIGHT_IMG_PATH = os.path.join(BASE_DIR, "images", "right.png")

# Load data
try:
    data = pandas.read_csv(DATA_PATH)
except FileNotFoundError:
    original_data = pandas.read_csv(ORIGINAL_DATA_PATH)
    data_dict = original_data.to_dict(orient="records")
except ValueError:
    original_data = pandas.read_csv(ORIGINAL_DATA_PATH)
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(canvas_text, text="French", fill="black")
    canvas.itemconfig(canvas_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_png)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_text, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=current_card["English"], fill='white')
    canvas.itemconfig(canvas_image, image=card_back_png)


def is_known():
    data_dict.remove(current_card)
    learn_data = pandas.DataFrame(data_dict)
    learn_data.to_csv(DATA_PATH, index=False)  # Save in the same directory
    next_card()


# ------------------ UI Setup ------------------ #
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_png = PhotoImage(file=CARD_FRONT_PATH)
card_back_png = PhotoImage(file=CARD_BACK_PATH)
canvas_image = canvas.create_image(400, 263, image=card_front_png)
canvas.grid(column=0, row=0, columnspan=2)
canvas_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

wrong_png = PhotoImage(file=WRONG_IMG_PATH)
wrong_button = Button(image=wrong_png, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_png = PhotoImage(file=RIGHT_IMG_PATH)
right_button = Button(image=right_png, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

next_card()
window.mainloop()
