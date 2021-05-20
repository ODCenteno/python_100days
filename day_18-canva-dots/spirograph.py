import turtle as t
from turtle import Screen
from colors import colors
from random import randint, choice

t.colormode(255)
color = (randint(0, 255), randint(0, 255), randint(0, 255))

def run(turtle, gap):
    turtle.speed(0)
    for _ in range(int(360/gap)):
        turtle.setheading(turtle.heading() + gap)
        turtle.fd(1)
        turtle.color(color)
        turtle.circle(100)


if __name__ == '__main__':
    gap = int(input("Set a gap number: "))
    turtle = t.Turtle()
    run(turtle, gap)
    screen = Screen()
    screen.exitonclick()