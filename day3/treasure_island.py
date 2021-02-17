


def main():

    left_or_right = input(f'You started walking and suddenly the road forks. Do you go right o left (type right o left)?: ').lower().strip()

    if left_or_right == 'left':
        swim_or_wait = input(f'You get to a big river and need to choose between "wait" or "swim"?: ').lower().strip()
        if swim_or_wait == 'wait':
            doors = input(f'after a 5 minutes brake you can see three doors. Which one do you open red, bue or yellow?: ').lower().strip()
            if doors == 'yellow':
                print(f'Congratulations, you find a digital wallet with 10000 Bitcoins!!!')
            else:
                print(f"Wrong doors, you walked into cannibal's house and you became dinner, game over")
        else:
            print(f'A big shark catch you with his sharp teeth, Game Over')
    else:
        print(f'You find a Ron barrel and got drunk till die, Game Over!')


if __name__ == '__main__':
    print('''
    *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("\nWelcome to Treasure Island.\n")
    print("Your mission is to find the treasure.")
    main()