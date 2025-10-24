from tkinter import *

def convert():
    try:
        miles = float(miles_input.get())
        km = round(miles * 1.60934, 2)
        kilo_result_label.config(text=f"{km}")
    except ValueError:
        kilo_result_label.config(text="Invalid input")

window = Tk()
window.title("Miles to Kilometer Converter")
window.geometry("500x300")  # Make the window bigger
window.config(padx=30, pady=30, bg="#f0f0f0")  # Add padding and background color

# Main frame for better organization
main_frame = Frame(window, bg="#f0f0f0")
main_frame.pack(expand=True, fill="both")

# Title label
title_label = Label(main_frame, text="Miles to Kilometers Converter", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333")
title_label.grid(column=0, row=0, columnspan=3, pady=(0, 20))

# Entry for miles
miles_input = Entry(main_frame, width=15, font=("Arial", 14))
miles_input.grid(column=1, row=1, padx=10, pady=10)

# Miles label
miles_label = Label(main_frame, text="Miles", font=("Arial", 14), bg="#f0f0f0")
miles_label.grid(column=2, row=1)

# Is equal to label
is_equal_label = Label(main_frame, text="is equal to", font=("Arial", 14), bg="#f0f0f0")
is_equal_label.grid(column=0, row=2)

# Kilometer result label
kilo_result_label = Label(main_frame, text="0", font=("Arial", 16, "bold"), bg="#e0e0e0", relief="sunken", width=10)
kilo_result_label.grid(column=1, row=2, padx=10, pady=10)

# Kilometer label
kilometer_label = Label(main_frame, text="Km", font=("Arial", 14), bg="#f0f0f0")
kilometer_label.grid(column=2, row=2)

# Calculate button
calculate_button = Button(main_frame, text="Calculate", command=convert, font=("Arial", 14), bg="#4CAF50", fg="white", relief="raised", padx=20, pady=5)
calculate_button.grid(column=1, row=3, pady=(20, 0))

window.mainloop()
