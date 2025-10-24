import pandas
import os
from tkinter import *
from tkinter import messagebox

# Load the NATO phonetic alphabet data
BASE_DIR = os.path.dirname(__file__)
IMAGE_PATH = os.path.join(BASE_DIR, "nato_phonetic_alphabet.csv")

try:
    data = pandas.read_csv(IMAGE_PATH)
    phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
except FileNotFoundError:
    messagebox.showerror("Error", "nato_phonetic_alphabet.csv not found in the current directory.")
    exit()

def generate_phonetic():
    word = word_input.get().upper()
    if not word:
        messagebox.showwarning("Warning", "Please enter a word.")
        return
    try:
        output_list = [phonetic_dict[letter] for letter in word]
        result_label.config(text=" ".join(output_list))
    except KeyError:
        messagebox.showerror("Error", "Sorry, only letters in the alphabet please.")
        word_input.delete(0, END)  # Clear the input

# Create the main window
window = Tk()
window.title("NATO Phonetic Alphabet Converter")
window.geometry("500x300")
window.config(padx=30, pady=30, bg="#f0f0f0")

# Main frame
main_frame = Frame(window, bg="#f0f0f0")
main_frame.pack(expand=True, fill="both")

# Title label
title_label = Label(main_frame, text="NATO Phonetic Alphabet Converter", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
title_label.grid(column=0, row=0, columnspan=2, pady=(0, 20))

# Input label
input_label = Label(main_frame, text="Enter a word:", font=("Arial", 14), bg="#f0f0f0")
input_label.grid(column=0, row=1, sticky="e", padx=(0, 10))

# Entry for word
word_input = Entry(main_frame, width=20, font=("Arial", 14))
word_input.grid(column=1, row=1, pady=10)

# Generate button
generate_button = Button(main_frame, text="Generate Phonetic Code", command=generate_phonetic, font=("Arial", 14), bg="#4CAF50", fg="white", relief="raised", padx=20, pady=5)
generate_button.grid(column=0, row=2, columnspan=2, pady=(20, 10))

# Result label
result_label = Label(main_frame, text="", font=("Arial", 14, "bold"), bg="#e0e0e0", relief="sunken", width=30, height=2, wraplength=400)
result_label.grid(column=0, row=3, columnspan=2, pady=(10, 0))

window.mainloop()
