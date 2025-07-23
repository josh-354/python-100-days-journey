from turtle import Turtle, Screen
import time
from car_manager import Car_manager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600,width=600)
screen.tracer(0)

screen.listen()
 
player=Player()
car_manager = Car_manager()

screen.listen()
screen.onkey(player.go_up,"w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()


screen.exitonclick()
