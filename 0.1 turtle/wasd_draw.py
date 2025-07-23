from turtle import Turtle,Screen

tika = Turtle()
screen = Screen()


def move_forward():
    tika.forward(10)

def move_backward():
    tika.backward(10)

def turn_right():
    tika.right(30)

def turn_left():
    tika.left(30)

def clear():
    tika.clear()
    tika.penup()
    tika.home()
    tika.pendown()


screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=turn_left)
screen.onkey(key="d",fun=turn_right)
screen.onkey(key="p",fun=clear)

screen.exitonclick()