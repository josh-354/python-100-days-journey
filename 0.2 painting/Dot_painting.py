#rgb_colors=[]
# Extract 6 colors from an image.
#colors = colorgram.extract('SpotPainting.jpg', 10)

#for color in colors:
#    r=color.rgb.r
#    g=color.rgb.g
#    b=color.rgb.b
#    new_color=(r,g,b)
#    rgb_colors.append(new_color)
#print(rgb_colors)

import colorgram
from turtle import Turtle, Screen, colormode
import random

# Set RGB color mode for Turtle
colormode(255)

# Set up screen and turtle
screen = Screen()
tika = Turtle()
tika.penup()

tika.hideturtle()



# Predefined list of RGB color tuples
color_list = [
    (211, 222, 215),
    (124, 37, 25),
    (222, 225, 228),
    (166, 105, 57),
    (6, 57, 83),
    (186, 158, 54),
    (109, 68, 84)
]


tika.setheading(225)
tika.forward(300)
tika.setheading(0)
number_of_dots=100
tika.speed("fastest")

for dot_count in range(1,number_of_dots+1):
    tika.dot(40, random.choice(color_list))
    tika.forward(50)

    if dot_count % 10==0:
        tika.setheading(90)
        tika.forward(50)
        tika.setheading(180)
        tika.forward(500)
        tika.setheading(0)


# Close window on click
screen.exitonclick()
