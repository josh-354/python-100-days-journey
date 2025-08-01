from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
IMAGE = "0.9 pomodoro/tomato.png"
reps=0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1
    
    work_sec = WORK_MIN*60
    short_break_sec= SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN *60

   
    if reps % 8 ==0:
        count_down(long_break_sec)
    elif reps % 2 ==0:
        count_down(short_break_sec)
    else:
        count_down(long_break_sec)

    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec <10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000,count_down,count-1)
    


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)



title_label = Label (text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))
title_label.grid(column=1,row=0)


canvas = Canvas(width=200, height=224,bg =YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file=IMAGE)
canvas.create_image(100,112,image =tomato_img)
timer_text = canvas.create_text(100,130,text = "00:00", fill="white",font =(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)



start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",highlightthickness=0)
reset_button.grid(column=2,row=2,)


check_mark = Label(text="✓",fg=GREEN,bg=YELLOW)
check_mark.grid(column=1,row=3)


window.mainloop()
