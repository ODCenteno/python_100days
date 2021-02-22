"""
Instructions
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25

Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: + $1
"""

def main():
    select_pizzas = sizes()

    add_peperoni = input('\nWould you like to add peperoni?(Y/N): ').upper()
    add_cheese = input('\nWould you like to add extra cheese for $1?(Y/N): ').upper()

    if add_peperoni == 'Y':
        if add_cheese == 'Y':
            total_price = calc_peperoni_price(select_pizzas) + select_pizzas[3]
            print(f'Your bill is ${total_price}\nThank you!')
        else:
            calc_peperoni_price(select_pizzas)
    elif add_peperoni == 'N' and add_cheese == 'Y':
        total_price = calc_only_pizza_price(select_pizzas) + select_pizzas[3]
        print(f'Your bill is ${total_price}\nThank you!')
    else:
        calc_only_pizza_price(select_pizzas)


def calc_only_pizza_price(select_pizzas):
    
    bill = []
    for pizza in select_pizzas:
        if pizza == 0:
            continue
        elif select_pizzas[0]:
            bill.append(select_pizzas[0] * 15)
        elif select_pizzas[1]:
            bill.append(select_pizzas[1] * 20)
        elif select_pizzas[2]:
            bill.append(select_pizzas[0] * 25)
    
    bill = sum(bill)
    print(f'Total only pizza bill is ${bill}')
    return bill

    # small_bill = select_pizzas[0] * 15
    # medium_bill = select_pizzas[1] * 20


    # bill = sum[x*b for x in select_pizzas[0, 3] select_pizzas[0] b == 15  select_pizzas[1] b == 20 and select_pizzas[2] b == 25]
    # print(f'Basic bill is ${bill}')


def calc_peperoni_price(select_pizzas):
    pass


def sizes():
    print(f'We have three sizes: small, medium and large\nPlease choose how many pizzas of each size do you want.')

    small = int(input('How many small pizzas do you want?: '))
    medium = int(input('How many small pizzas do you want?: '))
    large = int(input('How many small pizzas do you want?: '))

    number_of_pizzas = sum(small, medium, large)
    print(f'\nthe total number of ordered pizzas is {number_of_pizzas}\n')

    return [small, medium, large, number_of_pizzas]


if __name__ == '__main__':
    print('\nWelcome to My Pizzeria\n\n')
    main()