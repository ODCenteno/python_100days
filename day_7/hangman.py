import random


def welcome():
    print(f'{"*" * 100}\n\n')
    print("""
                                                                                               
    88        88                                                                               
    88        88                                                                               
    88        88                                                                               
    88aaaaaaaa88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba, 8b,dPPYba,   
    88        88 ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8 88P'   `"8a  
    88        88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88 88       88  
    88        88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88 88       88  
    88        88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8 88       88  
                                         aa,    ,88                                            
                                          "Y8bbdP"                                             """)

    print(f'\n\n{"*" * 100}\n\n')

def get_random_word():
    word_list = ["ardvark", "baboon", "camel"]
    chosen_word = random.choice(word_list)
    return chosen_word

def get_under_word(chosen_word):
    display = ['_' for letter in chosen_word]
    return display


def get_user_letter():
    
    guess = input(f'\nGuess a new letter: \n').lower().strip()
    return guess


def match_guess(chosen_word, display, stages, guess, lives):
    word_lenght = len(chosen_word)

    for i in range(word_lenght):
        letter = chosen_word[i]
        if guess == letter:
            display[i] = letter
    return display

def main():

    stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
    chosen_word = get_random_word()
    list_chosen_word = [x for x in chosen_word]
    display = get_under_word(chosen_word)
    print(f'This is the word that you are looking for: {display}')
    lives = 6
    game_over = False

    while not game_over:
        if display == list_chosen_word:
            print('We did it, You Won!')
            game_over = True
        elif lives > 0:
            guess = get_user_letter()
            if guess in chosen_word:
                current_display = match_guess(chosen_word, display, stages, guess, lives)
                print(stages[lives])
                print(f'You guessed one letter!')
                print(f'\n{current_display}')
            elif guess not in chosen_word:
                print(stages[lives])
                print(current_display)
                lives -= 1
                print(f'\n You have {lives} lives left')
        else:
            print(stages[0])
            print('Sorry,You Lose')
            game_over = True


if __name__ == '__main__':
    welcome()
    main()

