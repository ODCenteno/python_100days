import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.title("Super Turtle Crossing Road Game")

    # Create the Turtle that will cross the road
    crossturtle = Player()
    screen.listen()
    screen.onkey(crossturtle.move, key='Up')

    # Create the Car Manager that go to manage the car creation and move
    car_manager = CarManager()
    car_manager.create_car()
    running = True
    if running:
        screen.ontimer(car_manager.create_car(), 50)

    # Display the initial level
    game_score = Scoreboard()
    game_score.add_score()

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        car_manager.create_car()
        car_manager.run_car()

        # Increasing levels when the turtle successfully cross
        if crossturtle.ycor() == 280:
            crossturtle.goal()
            car_manager.level_up()
            game_score.update_score()

        if game_score.level > 8:
            car_manager.create_car()
            car_manager.create_car()
            car_manager.create_car()
            car_manager.create_car()
            car_manager.create_car()
        elif game_score.level > 5:
            car_manager.create_car()
            car_manager.create_car()
        elif game_score.level > 3:
            car_manager.create_car()

        # Detecting collision with the cars
        for car in car_manager.cars:
            if car.distance(crossturtle) < 15:
                game_is_on = False

    game_score.is_game_over()

    screen.exitonclick()


if __name__ == '__main__':
    main()
