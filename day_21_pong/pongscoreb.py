from turtle import Turtle

ALIGNMENT = "center"
FONT = ("helvetica", 64, "bold")


class Scoreboard(Turtle):
    def __init__(self, cords=(0, 280)):
        self.cords = cords
        super().__init__()
        self.ht()
        self.goto(0, 0)
        self.penup()
        self.color("#fed049")
        self.score = 0

    def add_score(self):
        self.goto(self.cords)
        self.write(arg=f"{self.score}", align=ALIGNMENT, font=FONT)

    def add_line(self):
        self.goto(self.cords)
        self.setheading(270)
        self.pensize(5)
        for _ in range(19):
            self.pendown()
            self.fd(15)
            self.penup()
            self.fd(15)

    def update_score(self):
        self.clear()
        self.penup()
        self.color("#fed049")
        self.goto(self.cords)
        self.score += 1
        self.add_score()
