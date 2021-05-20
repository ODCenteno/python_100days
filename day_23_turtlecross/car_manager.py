import random
from turtle import Turtle
from random import choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 8
MOVE_INCREMENT = 4
YCORDS = [y for y in range(-240, 280, 25)]


class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        print(self.cars)

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.goto(300, choice(YCORDS))
            new_car.setheading(180)
            self.cars.append(new_car)

    def run_car(self):
        for car in self.cars:
            car.fd(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT



