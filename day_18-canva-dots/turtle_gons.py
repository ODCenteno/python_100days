from turtle import Turtle, Screen
from random import randint
from colors import colors

class Shapes:

    def __init__(self, angle=90, rounds=4):
        self.angle = angle
        self.rounds = rounds
        self.forward = 100

    def draw(self):
        my_turtle = Turtle()
        my_turtle.pencolor(colors[randint(0, 8)])
        for _ in range(self.rounds):
            my_turtle.fd(self.forward)
            my_turtle.left(self.angle)


if __name__ == '__main__':
    new_turtle = Turtle()
    square = Shapes()
    square.draw()
    triangle = Shapes(120, 3)
    triangle.draw()
    pentagon = Shapes(72, 5)
    pentagon.draw()
    hexagon = Shapes(60, 6)
    hexagon.draw()
    heptagon = Shapes(51.428, 7)
    heptagon.draw()
    octagon = Shapes(45, 8)
    octagon.draw()
    nonagon = Shapes(40, 9)
    nonagon.draw()
    decagon = Shapes(36, 10)
    decagon.draw()

    screen = Screen()
    screen.colormode(255)
    screen.exitonclick()

