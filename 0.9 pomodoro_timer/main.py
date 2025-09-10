# Pomodoro

import tkinter as tk
import os

# ---------------------- CONSTANTS ---------------------- #
INITIAL_REPS = 4
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Colors
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# ---------------------- HELPER FUNCTIONS ---------------------- #
def split_time(time):
    """Returns time as MM:SS string."""
    minutes = time // 60
    seconds = time % 60
    return f"{format_time(minutes)}:{format_time(seconds)}"

def format_time(num):
    """Formats number with leading zero."""
    return f"{num:02}"

# ---------------------- COUNTDOWN ---------------------- #
def count_down(count):
    canvas.itemconfig(timer_text, text=split_time(count))
    if count > 0:
        params["timer"] = root.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------- TIMER START ---------------------- #
def start():
    if params["timer"] is None:
        start_timer()

def start_timer():
    checkmarks = "✔" * params["checks"]
    check_label.config(text=checkmarks)

    if params["reps_left"] == 0 and params["breaks_left"] == 0:
        reset()
    elif params["reps_left"] == 0 and params["breaks_left"] == 1:
        timer_label.config(text="Break", fg=RED)
        params["breaks_left"] -= 1
        count_down(LONG_BREAK_MIN * 60)
    elif params["reps_left"] < params["breaks_left"]:
        timer_label.config(text="Break", fg=PINK)
        params["breaks_left"] -= 1
        count_down(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text="Work", fg=GREEN)
        params["reps_left"] -= 1
        params["checks"] += 1
        count_down(WORK_MIN * 60)

# ---------------------- RESET ---------------------- #
def reset():
    if params["timer"]:
        root.after_cancel(params["timer"])
    reset_params()
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")

def reset_params():
    params["reps_left"] = INITIAL_REPS
    params["breaks_left"] = INITIAL_REPS
    params["checks"] = 0
    params["timer"] = None

# ---------------------- INIT PARAMS ---------------------- #
params = {}
reset_params()

# ---------------------- UI SETUP ---------------------- #
root = tk.Tk()
root.title("Pomodoro")
root.config(padx=100, pady=50, bg=YELLOW)

# Image path setup
BASE_DIR = os.path.dirname(__file__)
IMAGE_PATH = os.path.join(BASE_DIR, "tomato.png")

# Left column: Start
start_btn = tk.Button(text="Start", fg="grey", bg=GREEN, font=(FONT_NAME, 11),
                      width=6, relief="ridge", command=start)
start_btn.grid(row=2, column=0, padx=20)

# Middle column: Timer label
timer_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 36))
timer_label.grid(row=0, column=1, pady=4)

# Canvas with image
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
bg_image = tk.PhotoImage(file=IMAGE_PATH)
canvas.create_image(100, 112, image=bg_image)
canvas.grid(row=1, column=1)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))

# Checkmark label
check_label = tk.Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18), width=10)
check_label.grid(row=3, column=1)

# Right column: Reset
reset_btn = tk.Button(text="Reset", fg="grey", bg=PINK, font=(FONT_NAME, 11),
                      width=6, relief="ridge", command=reset)
reset_btn.grid(row=2, column=2, padx=12)

# Main loop
root.mainloop()
