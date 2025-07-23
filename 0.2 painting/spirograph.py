from turtle import Turtle, Screen
import random

tika = Turtle()
screen = Screen()

# Set screen to use RGB colors
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)  # No need to store in a variable


tika.shape("turtle")
tika.color(random_color())
tika.speed("fastest")


    

def draw_spirograph(size_of_gap):
    for n in range(int(360/size_of_gap)):
        tika.circle(100)
        current_heading = tika.heading()
        tika.setheading(current_heading +10)
        tika.circle(100)

draw_spirograph(5)



screen.exitonclick()
