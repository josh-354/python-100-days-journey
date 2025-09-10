import turtle
import pandas as pd
import os

# ---------------------------- FILE PATH SETUP ---------------------------- #
BASE_DIR = os.path.dirname(__file__)
IMAGE_PATH = os.path.join(BASE_DIR, "blank_states_img.gif")
CSV_PATH = os.path.join(BASE_DIR, "50_states.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "states_to_learn.csv")

# ---------------------------- SCREEN SETUP ---------------------------- #
screen = turtle.Screen()
screen.title("US State Game")
screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)

# ---------------------------- LOAD DATA ---------------------------- #
data = pd.read_csv(CSV_PATH)
all_states = data.state.to_list()
guessed_states = []

# ---------------------------- GAME LOOP ---------------------------- #
while len(guessed_states) < 50:
    answer = screen.textinput(
        title=f"{len(guessed_states)}/50 US States",
        prompt="What's another state's name? (Type 'Exit' to quit)"
    )

    if not answer:
        continue  # if user closes dialog

    answer = answer.title()

    if answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        pd.DataFrame(missing_states).to_csv(OUTPUT_PATH)
        break

    if answer in all_states and answer not in guessed_states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        answer_data = data[data.state == answer]
        t.goto(answer_data.x.item(), answer_data.y.item())
        t.write(answer)

screen.exitonclick()
