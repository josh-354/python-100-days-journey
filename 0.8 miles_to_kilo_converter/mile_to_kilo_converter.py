from tkinter import *

def convert():
    miles = float(miles_input.get())
    km = round(miles * 1.60934, 2)
    kilo_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Miles label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# is equal to label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# Kilometer result label
kilo_result_label = Label(text="0")
kilo_result_label.grid(column=1, row=1)

# Kilometer label
kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

# Button
calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)

window.mainloop()
