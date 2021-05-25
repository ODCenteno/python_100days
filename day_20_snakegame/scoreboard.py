from turtle import Turtle
import time

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
        with open("data.txt", mode="r", encoding="utf-8") as d:
            self.high_score = int(d.read())
        self.update_board()

    def update_board(self):
        self.clear()
        self.goto(0, 260)
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def track_score(self):
        self.penup()
        self.color("#ffffff")
        self.goto(0, 260)
        self.score += 1
        self.update_board()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"Game Over\nFinal Score: {self.score}\nHigh Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        self.goto(0, -50)
        # self.write(arg=f"\n\nTo play again type Enter", align=ALIGNMENT, font=FONT)
        time.sleep(2)
        self.update_board()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w", encoding="utf-8") as d:
                d.write(f"{self.high_score}")
        self.score = 0
        self.update_board()


