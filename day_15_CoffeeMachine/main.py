"""This is a Program inspired to reproduce a Coffee Machine"""

from art import logo
from menu import resources as rsc, coins
from menu import MENU as menu
import os
import time
import sys


def welcome():
    """Prompt show to user the options to make a good cup of coffee"""
    #os.system('clear')
    print(f"\n{'*' * 80}")
    print(f"\n\n{logo[1]['banner']}")
    print(f"{logo[0]['machine']}")


def get_order():
    """Ask the user for the kind of coffee to order"""
    response = False
    while not response:
        order = input(f"What would you like?\n[1]. Espresso\n[2]. Latte\n[3]. Cappuccino\nType the number to continue: ").lower().strip()
        if order == "1" or order == "2" or order == "3" or order == "off" or order == "report":
            response = True
    return order


def check_resources(user_choice):
    """Check if there are enough resources to make that drink"""

    if user_choice == '1':
        type_of_coffee = "espresso"
        coffee_cost = menu['espresso']['cost']
        coffee_ingredients = menu['espresso']['ingredients']
        #time.sleep(6)
    elif user_choice == '2':
        type_of_coffee = "latte"
        coffee_cost = menu['latte']['cost']
        coffee_ingredients = menu['latte']['ingredients']
        #time.sleep(6)
    elif user_choice == '3':
        type_of_coffee = "cappuccino"
        coffee_cost = menu['cappuccino']['cost']
        coffee_ingredients = menu['cappuccino']['ingredients']
        #time.sleep(6)

    machine_resources = rsc
    if machine_resources['water'] >= coffee_ingredients['water'] and machine_resources['milk'] >= coffee_ingredients['milk'] and machine_resources['coffee'] >= coffee_ingredients['coffee']:
        return [type_of_coffee, coffee_cost, coffee_ingredients]
    elif machine_resources['water'] < coffee_ingredients['water']:
        print(f"Sorry there is not enough water.")
        return "stand_by"
    elif machine_resources['milk'] < coffee_ingredients['milk']:
        print(f"Sorry there is not enough milk.")
        return "stand_by"
    elif machine_resources['coffee'] < coffee_ingredients['coffee']:
        print(f"Sorry there is not enough coffee.")
        return "stand_by"


def report(profit):
    """Generate a report that shows the current resources"""
    print(f"""The current resource values are:
Water: {rsc["water"]}ml
Milk: {rsc["milk"]}ml
Coffee: {rsc["coffee"]}g
Money: {profit}""")
    time.sleep(10)

def process_coins(coffee_cost):
    """Prompt to the user the amount to pay with coins"""
    print(f"Please insert the coins...")
    pennies_coins = int(input("Number of pennies inserted: "))
    nickles_coins = int(input("Number of nickles inserted: "))
    dimes_coins = int(input("Number of dimes inserted: "))
    quarters_coins = int(input("Number of quarters inserted: "))

    value_inserted = ((pennies_coins * coins["pennies"]) + (nickles_coins * coins["nickles"]) + (dimes_coins * coins["dimes"]) + (quarters_coins * coins["quarters"]))
    print(f"You inserted: ${round(value_inserted, 2)} dollars")
    time.sleep(5)
    proceed = check_transaction(value_inserted, coffee_cost)
    return proceed

def check_transaction(coins_value, coffee_cost):
    """Check that the user has inserted enough money to purchase the drink they selected"""
    if coins_value == coffee_cost:
        add_profit = coffee_cost
        return True
    elif coins_value > coffee_cost:
        change = round((coins_value - coffee_cost), 2)
        print(f"Here is ${change} dollars in change.")
        time.sleep(3)
        add_profit = coffee_cost
        return True, add_profit
    else:
        print(f"Sorry, that is not enough money. Money refunded.")
        return False

def make_coffee():
    """Show time and the coffee is made with the resources that then are deducted from the coffee machine resources"""
    pass


def power():
    """Function that can turn off or on the machine"""
    print(f'Turning off...')
    time.sleep(4)
    sys.exit()


if __name__ == '__main__':
    turn_off = False
    profit = 0
    while not turn_off:
        welcome()
        user_choice = get_order()

        if user_choice == "off":
            power()
            turn_off = True
            continue

        elif user_choice == "report":
            report(profit)
            continue

        getting_ready = check_resources(user_choice)

        if getting_ready == "stand_by":
            print(f'We should wait for the technician to fill the machine ')
            time.sleep(6)
            continue
        elif getting_ready != "stand_by":
            print(f"You Select: {getting_ready[0]}.\n")
            print(f"The cost of the {getting_ready[0]} is ${getting_ready[1]}.")
            check_pay = process_coins(getting_ready[1])
            if check_pay:
                make_coffee()
                profit = getting_ready[1]
            else:
                time.sleep(5)
                continue
