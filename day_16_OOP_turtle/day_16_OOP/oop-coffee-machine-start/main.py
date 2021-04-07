from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# coffee1 = MenuItem("name", "water", "milk", "coffee", "cost")
# coffee1.name = "espresso"
# coffee1.cost = 1.5
# coffee1.ingredients = {
#     "water": 50,
#     "milk": 0,
#     "coffee": 18,
# }
#
# coffee_latte = MenuItem("name", "water", "milk", "coffee", "cost")
# coffee_latte.name = "latte"
# coffee_latte.cost = 2.5
# coffee_latte.ingredients = {"water": 200, "milk": 150, "coffee": 24}
#
# coffee_cappu = MenuItem("name", "water", "milk", "coffee", "cost")
# coffee_cappu.name = "cappuccino"
# coffee_cappu.cost = 3.0
# coffee_cappu.ingredients = {
#     "water": 250,
#     "milk": 100,
#     "coffee": 24,
# }

new_menu = Menu()


def welcome():
    print(f"\n\n{'*' * 80}")
    print(f"\n\n\tTHE COFFEE MACHINE MACHINE\n\n")


def menu():
    global new_menu
    display_menu = new_menu.get_items()
    print(f"This Coffee Chop Menu is: {display_menu}")
    user_choice = input(f'What would you like to order {display_menu}: ').lower().strip()
    # user_order = MenuItem("name", "water", "milk", "coffee", "cost")
    # user_order.cost = f"{user_order.name}"
    # print(f"The {user_order} is ${user_order.cost}")
    return user_choice


def check_resources(user_order):
    global new_menu
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    if user_order == 'report':
        new_report = CoffeeMaker()
        return new_report.report()
    elif user_order == 'off':
        is_on = False
        return is_on
    else:
        new_drink = new_menu.find_drink(user_order)
        coffee_machine = CoffeeMaker()
        if coffee_machine.is_resource_sufficient(new_drink) and money_machine.make_payment(new_drink.cost):
            coffee_maker.make_coffee(user_order)

    # kitchen = MenuItem("name", "water", "milk", "coffee", "cost")
    # recipe_water = kitchen["water"]
    # recipe_milk = kitchen["milk"]
    # recipe_coffee = kitchen["coffee"]
    # coffee_machine = CoffeeMaker()
    # check_resources = coffee_machine.is_resource_sufficient(f"{user_order}: {coffee_ingredients}")
    # if check_resources:
    #     coffee_machine.make_coffee(user_order)

    # menu_item = menu.find_drink(user_order)


if __name__ == '__main__':
    is_on = True
    while is_on:
        welcome()
        order = menu()
        resources_sufficient = check_resources(order)
        if resources_sufficient:
            pass
