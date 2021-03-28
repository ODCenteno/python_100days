

import random
import os, time

LOGO = """
╔═╗╦ ╦╔═╗╔═╗╔═╗╔╦╗╔═╗                  
╠═╣║║║║╣ ╚═╗║ ║║║║║╣                   
╩ ╩╚╩╝╚═╝╚═╝╚═╝╩ ╩╚═╝                  
╔╗╔╦ ╦╔╦╗╔╗ ╔═╗╦═╗  ╔═╗╔═╗╔═╗╔═╗╦╔╗╔╔═╗
║║║║ ║║║║╠╩╗║╣ ╠╦╝  ║ ╦╠═╣╚═╗╚═╗║║║║║ ╦
╝╚╝╚═╝╩ ╩╚═╝╚═╝╩╚═  ╚═╝╩ ╩╚═╝╚═╝╩╝╚╝╚═╝
╔═╗╔═╗╔╦╗╔═╗                           
║ ╦╠═╣║║║║╣                            
╚═╝╩ ╩╩ ╩╚═╝                           
"""

def welcome():
    os.system('clear')
    print(f"\n\n{'*'*100}\n\n{LOGO}\n\n{'*'*100}")
    print(f'\n\nWelcome to the Number Guessing Game!\n\n')

def game_level():
    level = ''
    while level != 'easy' or level != 'hard':
        level = input(f"    Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
        if level == 'easy' or level == 'hard':
            print(f"\nI'm thinking of a number between 1 and 100.")
            return level

def main(difficulty):
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 6
    
    goal_number = random.randint(1, 100)

    while attempts > 0:
        print(f'You have {attempts} attemps to guess the number.')
        guess = int(input('Make a guess: '))
        if guess == goal_number:
            print(f'You got it!\nThe anwers was {goal_number}!')
            time.sleep(2)
            break
        elif guess < goal_number:
            print(f'Too low\nGuess again.\n\n')
            time.sleep(1.5)
            attempts -= 1
        elif guess > goal_number:
            print(f'Too high\nGuess again.\n\n')
            time.sleep(1.5)
            attempts -= 1
    
    if attempts == 0:
        print(f'You lose\nTry again!')


if __name__ == '__main__':
    welcome()
    boring = False
    while not boring:
        level = game_level()
        main(level)
        keep_playing = input('Do you want to play again? [Y/N]: \n').lower().strip()
        if keep_playing == 'n':
            print(f'Thank you to have fun with us\nBye!')
            boring = True
