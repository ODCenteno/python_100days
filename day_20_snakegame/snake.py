from turtle import Turtle
START = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self, snake_color="#007580"):
        self.squares = []
        self.color = snake_color
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for position in START:
            self.add_segment(position)

    def add_segment(self, position):
        square = Turtle("square")
        square.color(self.color)
        square.penup()
        square.goto(position)
        self.squares.append(square)

    def extend(self):
        self.add_segment(self.squares[-1].position())

    def snake_moves(self):
        for i in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[i - 1].xcor()
            new_y = self.squares[i - 1].ycor()
            self.squares[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.squares[0].setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.squares[0].setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.squares[0].setheading(180)
