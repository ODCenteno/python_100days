"""
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
"""

import random
from art import logo
from rules import rules
import time


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def welcome():
    print(logo[0])

def instructions():
    print(f'\n\n########################### Our Blackjack House Rules #################################\n\n')
    print(f'{rules[0]}\n\n')

def get_ready(round = 1):

    if round == 1:
        ready = False
        while not ready:
            launch = input(f'Are you ready to play? (Y/N): ').lower().strip()
            if launch == 'y':
                ready = True
    # elif round > 1:
    #     ready = False
    #     while not ready:
    #         launch = input(f'Do you want to play again? (Y/N): ').lower().strip()
    #         if launch == 'y':
    #             ready = True
    #         elif launch == 'n':

    
    print(f'\nShuffling the cards deck...\n\n')
    time.sleep(1.5)
    print(f'Round {round}, two cards delivery...\n\n')
    time.sleep(1.5)


def get_card():

    new_card = random.choice(cards)
    return new_card


def run():
    dealer_cards = [random.choice(cards) for card in range(2)]
    player_cards = [random.choice(cards) for card in range(2)]
    
    print(f"The dealer's card is {dealer_cards[0]}\n")
    print(f"The Player's cards are {player_cards}\n")
    
    # Check Score
    dealer_score = sum([ x for x in dealer_cards])
    print(f"The dealer's score is {dealer_score}")
    player_score = sum([x for x in player_cards])
    print(f"The player's score is {player_score}")

#     ask_player_new_card(dealer_cards, player_cards)

# def ask_player_new_card(dealer_cards, player_cards, dealer_score):
    # ready = False
    # while not ready:

    no_more_cards = False
    while not no_more_cards:
        ask_for_card = input('Do yoy want another card? (Y/N): ').lower().strip()
        if ask_for_card == 'y':
            player_cards.append(get_card())
            player_score = sum([x for x in player_cards])
            if player_score > 21 and 11 in player_cards:
                as_index = player_cards.index(11)
                player_cards[as_index] = 1
                player_score = sum([x for x in player_cards])
            print(f"The Player's cards are {player_cards}\n")
        elif ask_for_card == 'n':
            #return player_cards
            no_more_cards = True
    
    print(f"The Final player's score is {player_score}\n\n")

    while dealer_score < 17:
        dealer_cards.append(get_card())
        dealer_score = sum([ x for x in dealer_cards])

    check_winner(dealer_score, player_score)

    print(f"\n\nThe Final Dealer's score is {dealer_score}\n\n")


def check_winner(dealer_score, player_score):

    if player_score > 21:
        print('You lose')
    elif dealer_score > 21 and player_score <= 21:
        print('Player Win')
    elif dealer_score == player_score:
        print('You lose')
    elif dealer_score > player_score:
        print('You lose')
    else:
        print('Player Win')

    # drop_cards = True

    # while drop_cards:
    #     pass
    

def main():

    get_ready()
    round = 1
    boring = False
    while not boring:
        run()
        keep_playing = input(f'\n\nDo you want to play again (Y/N): \n\n').lower().strip()
        if keep_playing == 'y':
            print('\n\n¡Lets go!\n\n')
            time.sleep(1.5)
            get_ready(round + 1)
        elif keep_playing == 'n':
            boring = True


if __name__ == '__main__':
    welcome()
    instructions()
    main()
