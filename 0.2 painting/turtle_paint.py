from turtle import Turtle,Screen,colormode
import random

screen = Screen()
screen.bgcolor("blue")
colormode(255)
turtles=[]
forward=[10,20,30,40,50,60,70]
turn = tuple(range(-100, 100))


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)  # No need to store in a variable

def create_turtle():
    t = Turtle(shape="turtle")
    t.pensize(7)
    t.speed("fastest")
    t.color(random_color())
    turtles.append(t)

for n in range(30):
    create_turtle()

for i in range(200):
    for t in turtles:
        t.left(random.choice(turn))
        t.forward(random.choice(forward))



screen.exitonclick()