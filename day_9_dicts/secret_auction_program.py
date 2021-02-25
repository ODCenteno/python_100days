import os
from art import logo
from countdown import count_down

# Give a warm welcome to the program and bring the logo
def welcome():
    print(logo)
    print(f'Get fun while you bid with your friends')


def getting_bids():
    players_bid = {}
    add_player = True

# main logic of the program to add players and bids to  
    while add_player:
        try:
            player_name = input(f'Enter the player\'s name: ').title().strip()
            new_bid = float(input(f'Type {player_name}\'s bid: $ '))
            players_bid[player_name] = new_bid
        except ValueError:
            print(f'That is not a valid input')
            continue    # If ther is a value error input will start again to ask player's name and bid

        bid_finished = False # variable to start/stop the next while loop
        while not bid_finished:
            more_players = input('Is there any other player?[Y/N]: ').lower().strip()
            if more_players == 'y':
                bid_finished = True
                os.system('clear')
            elif more_players == 'n':    
                add_player = False  # Stops this loop
                bid_finished = True # Stops main loop
            else:
                print(f'That\'s not a valid option') 
                # If there is a ValueError we ask for the answer again
    return players_bid

def max_bid(bids):
    get_highest_bid = 0
    winner = ''

    for name, bid in bids.items():
        if bid > get_highest_bid:
            get_highest_bid = bid
            winner = name
    os.system('clear')
    count_down() # Prints a countdown before display the winner
    print(f'{"*"*80}\n\nThe winner is {winner}, who\'s bid was ${get_highest_bid}\n\n{"*"*80}\n\n')


if __name__ == '__main__':
    welcome()
    bids = getting_bids()
    winner = max_bid(bids)