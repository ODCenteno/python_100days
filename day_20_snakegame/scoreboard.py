from turtle import Turtle

ALIGNMENT = "center"
FONT = ("helvetica", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.color("#ffffff")
        self.goto(0, 260)
        self.score = 0
        self.update_board()

    def update_board(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def track_score(self):
        self.clear()
        self.penup()
        self.color("#ffffff")
        self.goto(0, 260)
        self.score += 1
        self.update_board()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"Game Over\nFinal Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(0, -50)
        self.write(arg=f"\n\nTo play again type Enter", align=ALIGNMENT, font=FONT)


