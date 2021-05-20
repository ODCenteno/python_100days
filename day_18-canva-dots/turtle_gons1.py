from turtle import Turtle, Screen
from random import randint

def square(my_turtle):
    # rgb_color = (randint(1, 256), randint(1, 256), randint(1, 256))
    # print(rgb_color)
    # my_turtle.color(get_color())
    for _ in range(4):
        my_turtle.fd(100);
        my_turtle.left(90);

def triangle(my_turtle):
    # global screen
    # screen.colormode()
    # my_turtle.pencolor(get_color())
    for _ in range(5):
        my_turtle.fd(100);
        my_turtle.left(72);

def pentagon(my_turtle):
    # my_turtle.color(get_color())
    # my_turtle.colormode(255)
    for _ in range(3):
        my_turtle.fd(100);
        my_turtle.left(120);

if __name__ == '__main__':
    new_turtle = Turtle()
    square(new_turtle)
    triangle(new_turtle)
    pentagon(new_turtle)
    hexagon(new_turtle)
    octagon(new_turtle)
    nonagon(new_turtle)
    decagon(new_turtle)

    screen = Screen()
    screen.exitonclick()

