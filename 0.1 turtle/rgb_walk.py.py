from turtle import Turtle, Screen
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

# Turtle appearance
tika.shape("turtle")
tika.pensize(2)
tika.speed(0)  # Fastest speed

# Drawing a beautiful colorful spiral
try:
    for i in range(200):
        tika.color(random_color())
        tika.forward(i * 2)  # Gradually increase forward distance for spiral effect
        tika.right(59)  # Turn by 59 degrees for a nice spiral pattern (approximates golden angle)
except Exception as e:
    print(f"Turtle drawing interrupted: {e}")

# Wait for user to click the screen to close
try:
    screen.exitonclick()
except:
    pass
