"""
Develop a Rock, Paper, Scissors game
"""
import random


def rules():

    print("""\n

                            ________       ________       ____   
                            `MMMMMMMb.     `MMMMMMMb.    6MMMMb\ 
                            MM    `Mb      MM    `Mb   6M'    ` 
                            MM     MM      MM     MM   MM       
                            MM     MM      MM     MM   YM.      
                            MM    .M9      MM    .M9    YMMMMb  
                            MMMMMMM9'      MMMMMMM9'         `Mb 
                            MM  \M\        MM                  MM 
                            MM   \M\       MM                  MM 
                            MM    \M\      MM          L     ,M9 
                            _MM_    \M\  __MM_         MYMMMM9  

    The game is played where players deliver hand signals that will represent the elements of the game; rock, paper and scissors.\n   The outcome of the game is determined by 3 simple rules:

    - Rock wins against scissors.
    - Scissors win against paper.
    - Paper wins against rock.\n\n
    """)

def game_items():
    rock = '''
        _______
    ---'   ____)
        (______)
        (_____:)
        (______)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _____
    ---'   __)
            ______
            ______)
        __________)
        (____)
    ---.__(___)
    '''

    items = [rock, paper, scissors]

    return items

def main(items):

    while True:
        ai_option = random.randint(0, 2)
        player_option = input('To play enter the number that correspond with your move:\n[0] for Rock\n[1] for Paper\n[2] for Scissors\n\n-> Type the number or Enter to quit: ')

        if player_option == '':
            break
        elif player_option == '0' or player_option == '1' or player_option == '2':
            player_option = int(player_option)
        else:
            print('\n\n XXX  -> That\'s not a valid option, Try again   XXX\n\n')
            main(items)


        if player_option == ai_option:
            print(f'\nPlayer choice:{items[player_option]}\n\nAI choice:{items[ai_option]}\n\n\nIt\'s a draw!\n\n')
        elif player_option == 0 and ai_option == 1:
            print(f'\nPlayer choice:\n\n{items[player_option]}\n\nAI choice:{items[ai_option]}\n\n\nYou Lose!\n\n')
        elif player_option == 1 and ai_option == 0:
            print(f'\nPlayer choice:\n\n{items[player_option]}\n\nAI choice:{items[ai_option]}\n\n\nYou WON!\n\n')
        elif player_option == 2 and ai_option == 0:
            print(f'\nPlayer choice:\n\n{items[player_option]}\n\nAI choice:{items[ai_option]}\n\n\nYou Lose!!\n\n')
        elif player_option == 1 and ai_option == 2:
            print(f'\nPlayer choice:\n\n{items[player_option]}\n\nAI choice:{items[ai_option]}\n\n\nYou Lose!!\n\n')
        elif player_option == 2 and ai_option == 1:
            print(f'\nPlayer choice:\n\n{items[player_option]}\n\nAI choice:{items[ai_option]}\n\n\nYou WON!!\n\n')
        elif player_option == 0 and ai_option == 2:
            print(f'\nPlayer choice:\n\n{items[player_option]}\n\nAI choice:{items[ai_option]}\n\n\nYou WON!!\n\n')

if __name__ == '__main__':
    rules()
    items = game_items()
    main(items)