from turtle import Turtle

ALIGMENT = "left"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, cords=(-270, 270)):
        self.cords = cords
        super().__init__()
        self.penup()
        self.color("black")
        self.ht()
        self.goto(cords)
        self.level = 1

    def add_score(self):
        self.goto(self.cords)
        self.write(arg=f"Level: {self.level}", align=ALIGMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.penup()
        self.goto(self.cords)
        self.level += 1
        self.add_score()

    def is_game_over(self):
        self.clear()
        self.penup()
        self.goto(0, 0)
        self.write(arg=f"   GAME OVER :(\n\n Sorry, you lost!\nYou reach level: {self.level}", align='center', font=FONT)

