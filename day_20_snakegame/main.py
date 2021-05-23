from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.colormode(255)
    screen.bgcolor("#282846")
    screen.title("Rapid and Furious Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, key='Up')
    screen.onkey(snake.down, key='Down')
    screen.onkey(snake.right, key='Right')
    screen.onkey(snake.left, key='Left')
    # screen.onkey(main, key='Enter')

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)

        snake.snake_moves()

        # Detect the collision between the snake and food:
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.track_score()

        # Detect the collision with the wall
        if snake.head.xcor() > 297 or snake.head.xcor() < -297 \
                or snake.head.ycor() > 297 or snake.head.ycor() < -297:
            scoreboard.game_over()
            scoreboard.reset_scoreboard()
            snake.reset_snake()

        # Detect collision with the tail
        for segment in snake.squares[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                scoreboard.reset_scoreboard()
                snake.reset_snake()


    screen.exitonclick()


if __name__ == '__main__':
    main()
