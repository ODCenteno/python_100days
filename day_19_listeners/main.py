from turtle import Turtle, Screen
from colors import colors
from random import choice

"""A Python program to sketch figures and draw with the keyboard
You can use de next keys:
- W = move forwards
- S = move backwards
- A = counter-clockwise
- D = clockwise
- C = clear and set to default position"""

# def run():
ajax = Turtle()
ajax.speed('fastest')


def forwards():
    ajax.color(choice(colors))
    ajax.forward(10)


def backwards():
    ajax.color(choice(colors))
    ajax.backward(10)


def counter_clock():
    ajax.color(choice(colors))
    ajax.setheading(ajax.heading() - 10)
    ajax.forward(10)


def clockwise():
    ajax.color(choice(colors))
    ajax.setheading(ajax.heading() + 10)
    ajax.forward(10)


def restart():
    screen.reset()


screen = Screen()
screen.colormode(255)
screen.listen()
screen.onkey(key='w', fun=forwards)
screen.onkey(key='s', fun=backwards)
screen.onkey(key='a', fun=counter_clock)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='c', fun=restart)
screen.exitonclick()
# if __name__ == '__main__':
#     run()
