from turtle import Turtle, Screen


class Template(Turtle):
    def __init__(self):
        super().__init__()
        self.new_screen()

    def new_screen(self):
        screen = Screen()
        screen.colormode(255)
        screen.setup(width=800, height=600)
        screen.bgcolor("#282846")
        screen.title("Awesome Pong Game")
        screen.tracer(0)
        draw_line()
        screen.exitonclick()

    def draw_line(self):
        turtle = Turtle()
        turtle.penup()
        turtle.goto(0, 200)
