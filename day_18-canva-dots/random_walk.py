import turtle as t
from turtle import Screen
from random import randint, choice
from colors import random_color

def main():
    total_steps = int(input(f"How many steps the drunken will make? Type a number: "))
    # borracho = RandomWalk()
    # borracho.walk()

    borracho = t.Turtle()
    borracho.width(4)
    borracho.speed(0)
    t.colormode(255)
    step_size = 15

    for _ in range(total_steps):
        towards = choice([0, 270, 180, 90])
        borracho.setheading(towards)
        borracho.pencolor(random_color)
        borracho.fd(step_size)

    screen = Screen()
    screen.screensize(600)
    screen.exitonclick()


# class RandomWalk:
#
#     def __init__(self, total_steps):
#         self.total_steps = total_steps
#         self.color = colors[randint(0, 8)]
#         self.step = 10
#
#     def walk(self):
#         my_turtle = Turtle()
#         towards = choice([0, 270, 180, 90])
#         print(towards)
#         for _ in range(total_steps):
#             my_turtle.setheading(self, towards)
#             my_turtle.pencolor(self.color)
#             my_turtle.fd(self.step)


if __name__ == '__main__':
    main()