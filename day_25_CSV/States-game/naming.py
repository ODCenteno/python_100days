from turtle import Turtle

FONT = ('Helvetica', 12, 'normal')

class Naming(Turtle):

    def __init__(self, name, cords):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(cords)
        self.write(arg=name, align='center', font=FONT)
