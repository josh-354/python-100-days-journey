import turtle
import pandas

screen = turtle.Screen()
screen.title("US state game")
IMAGE = "0.6 pandas/us_state/blank_states_img.gif"
screen.addshape(IMAGE)

turtle.shape(IMAGE)

data = pandas.read_csv("0.6 pandas/us_state/50_states.csv")
all_states = data.state.to_list()

guessed_states=[]

while len(guessed_states)<50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 states",prompt="whats another states name").title()


    if answer =="Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        df = pandas.DataFrame(missing_states)
        df.to_csv("0.6 pandas/us_state/states_to_learn.csv")
            
        break
    if answer in all_states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        answer_data = data[data.state==answer]
        t.goto(answer_data.x.item(),answer_data.y.item())
        t.write(answer)



screen.exitonclick()