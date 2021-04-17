from turtle import Screen
from snake import Snake
from food import Food
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

    screen.listen()
    screen.onkey(snake.up, key='Up')
    screen.onkey(snake.down, key='Down')
    screen.onkey(snake.right, key='Right')
    screen.onkey(snake.left, key='Left')

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)

        snake.snake_moves()

        if snake.head.distance(food) < 15:
            food.refresh()

    screen.exitonclick()


if __name__ == '__main__':
    main()
