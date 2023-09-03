COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager():
    def __init__(self):
        self.garage = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.goto(300, random.randint(-230, 230))
        self.garage.append(new_car)

    def move_car(self):
        for car in self.garage:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

#Final