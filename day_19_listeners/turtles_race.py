from turtle import Turtle, Screen
from colors import race_colors
from random import choice


screen = Screen()
screen.setup(width=600, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Choose the turtle that will win the race\n- Red\n - Blue\n - Green\n - Yellow\n - Purple\n - Orange\npick a color: ")
print(user_bet)


def create_turtle(y_pos, index_color):
    turtle = Turtle("turtle")
    turtle.penup()
    turtle.pensize(25)
    turtle.color(race_colors[index_color])
    turtle.goto(x=-280, y=y_pos)
    return turtle

init_y = -120
racers = []
index_color = 0
for i in range(6):
    new_racer = create_turtle(init_y, index_color)
    racers.append(new_racer)
    init_y = init_y + 50
    index_color += 1


for racer in racers:
    racer.forward()

screen.exitonclick()
