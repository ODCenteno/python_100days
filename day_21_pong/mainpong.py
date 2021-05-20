from turtle import Turtle, Screen
from random import randint
import time

from ball import Balls
from pongscoreb import Scoreboard
from paddles import Paddles

# TODO: Create a Canvas containing a line in the middle
# TODO: Create Players paddles: A class that make player interact with the ball and opponent
# TODO: Create ball and set movement and response to hits, detect wall and players collisions
# TODO: Create a Scoreboard: write score on screen and sum the points on each side
# TODO: Set game start: Set the position at center for players and ball
# TODO: Detect when a new point is made, keep score and reset the game
# TODO: End game and declare a winner

PCORDS = (-60, 220)
MCORDS = (60, 220)
PADDLE_PLAYER_START = [-350, 0]
PADDLE_AJAX_START = [350, 0]

def pong():
    ball_speed = 5
    screen = Screen()
    screen.colormode(255)
    screen.setup(width=800, height=600)
    screen.bgcolor("#282846")
    screen.title("Awesome Pong Game")
    screen.tracer(0)

    player = Paddles(PADDLE_PLAYER_START)
    ajax = Paddles(PADDLE_AJAX_START)
    ball = Balls()

    scoreboard = Scoreboard()
    scoreboard.add_line()

    player_score = Scoreboard(cords=PCORDS)
    ajax_score = Scoreboard(cords=MCORDS)
    player_score.add_score()
    ajax_score.add_score()

    screen.listen()
    screen.onkey(player.go_up, key='w')
    screen.onkey(player.go_down, key='s')
    screen.onkey(ajax.go_up, key='Up')
    screen.onkey(ajax.go_down, key='Down')

    def point_and_restart():
        ball.goto(0, 0)
        player.goto(PADDLE_PLAYER_START)
        ajax.goto(PADDLE_AJAX_START)
        time.sleep(2)

    game_is_on = True
    while game_is_on:
        screen.update()
        ball.move(ball_speed)

        # Wall Bouncing
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce()

        # Sum Point and restart the game
        if ball.xcor() > 390:
            player_score.update_score()
            point_and_restart()
            ball.setheading(randint(100, 230))
            ball_speed += 1
        elif ball.xcor() < -390:
            ajax_score.update_score()
            point_and_restart()
            ball.setheading(randint(0, 45))
            ball_speed += 0.5

        # Detect collision with the paddle
        if ball.distance(player) < 51 and ball.xcor() < -350 or ball.distance(ajax) < 51 and ball.xcor() > 350:
            ball.hit_bounce()


    screen.exitonclick()



if __name__ == '__main__':
    pong()
