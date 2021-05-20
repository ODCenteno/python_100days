from turtle import Turtle
from random import randint

class Balls(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#fed049")
        self.pensize(4)
        self.penup()
        self.setheading(randint(1, 360))

    def move(self, speed):
        self.fd(speed)

    def bounce(self):
        print(self.heading())
        if self.heading() > 0  and  self.heading() < 60:
            self.setheading(365 - self.heading())
        elif self.heading() > 59 and self.heading() < 91:
            self.setheading(370 - self.heading())
        elif self.heading() > 269  and  self.heading() < 301:
            self.setheading(80 - (self.heading() - 270))
        elif self.heading() > 300  and  self.heading() < 361:
            self.setheading(90 - (self.heading() - 270))
        elif self.heading() > 90  and  self.heading() < 180:
            self.setheading(270 - (self.heading() - 90))
        elif self.heading() > 179  and  self.heading() < 271:
            self.setheading(90 + (270 - self.heading()))

    def hit_bounce(self):
        if self.heading() > -1 and self.heading() < 91:
            self.setheading(185 - self.heading())
        elif self.heading() > 270 and self.heading() < 361:
            self.setheading(185 + (360 - self.heading()))
        elif self.heading() > 90 and self.heading() < 181:
            self.setheading(185 - self.heading())
        elif self.heading() > 180 and self.heading() < 271:
            self.setheading(365 - (self.heading() - 180))
