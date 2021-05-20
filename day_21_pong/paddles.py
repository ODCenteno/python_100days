from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddles(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("#fed049")
        self.start = position
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
