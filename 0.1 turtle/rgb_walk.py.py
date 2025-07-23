from turtle import Turtle, Screen, Terminator
import random

# Setup turtle and screen
tika = Turtle()
screen = Screen()
screen.colormode(255)

# Function to return a random RGB color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Settings
turns = [0, 90, 180]
size = [4]

# Turtle appearance
tika.shape("turtle")
tika.pensize(random.choice(size))
tika.speed(0)  # Fastest speed

# Drawing loop
try:
    for _ in range(200):
        tika.color(random_color())
        tika.forward(30)
        tika.setheading(random.choice(turns))
except Exception as e:
    print(f"Turtle drawing interrupted: {e}")

# Wait for user to click the screen to close
try:
    screen.exitonclick()
except:
    pass
