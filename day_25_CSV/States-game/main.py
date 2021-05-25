import turtle
from turtle import Turtle
from turtle import Screen
import pandas as pd
import csv

from naming import Naming

def run():
    data = pd.read_csv('50_states.csv')
    states = data[data.columns[0]]
    print(states)
    screen = Screen()
    screen.title('U.S. States Game')
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    # def get_mouse_click_cords(x, y):
    #     print(x, y)
    # turtle.onscreenclick(get_mouse_click_cords)

    is_guessing = True
    counter = 0
    guessed_states = []

    while is_guessing:
        answer_state = screen.textinput(title=f"{counter}/50 Guess the State", prompt="What's another State name?").title().strip()
        if answer_state == "Exit":
            missing_states = [x for x in states if x not in guessed_states]
            print(f'The states that you missed guessing are:\n{missing_states}')
            # save a list with the missing states to learn:
            new_data = pd.DataFrame(missing_states)
            new_data.to_csv('states_to_learn.csv')
            break

        for st in data['state']:
            if st == answer_state:
                guessed_states.append(answer_state)
                counter += 1
                state_data = data[data.state == answer_state]   # Obtiene los datos de la fila
                state_cords = (int(state_data.x), int(state_data.y))
                print_state = Naming(st, state_cords)
            #     place_state(answer_state)
            if counter == 51:
                is_guessing = False


if __name__ == '__name__':
    run()

