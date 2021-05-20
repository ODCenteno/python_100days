from turtle import Turtle, Screen
from colors import colors
import random


def shape(sides):
    turtle.color(random.choice(colors))
    angle = 360 / sides
    for _ in range(sides):
        turtle.fd(100)
        turtle.right(angle)

turtle = Turtle
for side in range(3, 10):
    shape(side)
