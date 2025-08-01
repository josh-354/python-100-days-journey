from turtle import Turtle
import random
COLORS = ["red","blue","yellow"]
MOVE_INCREMENT =10
STARTING_MOVE_DISTANCE = 5

class Car_manager:
    def __init__(self):
        self.all_cars=[]
    
    def create_cars(self):
        new_car=Turtle("square")
        new_car.shapesize(stretch_wid=2,stretch_len=1)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_y = random.randint(-250,250)
        new_car.goto(300,random_y)
        self.all_cars.append(new_car)

    
    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)