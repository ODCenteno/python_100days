# TODO: Print Report
# TODO: Check resources sufficient?
# TODO: Process coins
# TODO: Check transaction successful?
# TODO: make Coffee

from art import logo
from menu import MENU
from menu import coins
from menu import resources

def print_report():
    """Print a report of the current resources"""
    print(resources)
    print(f'water: {resources["water"]}ml')

def ask_user_for_drink():
    """Ask the user for the type of coffee and promp it in the screen"""
    print("\nWhat would you like to drink? Menu:\n[1] Espresso\n[2] Latte\n[3] Cappuccino")
    user_selection = input("Your selection: ")
    
    if user_selection == "1":
        print("You select Espresso")
    elif user_selection == "2":
        print("You select Latte")
    elif user_selection == "3":
        print("You select Cappuccino")
    
    return user_selection

def run():
    
    """Welcome message"""
    print(logo[0]["machine"])
    print(logo[1]["banner"])
    
    is_machine_on = True

    while is_machine_on:
        user_choice = ask_user_for_drink()
        
        if user_choice == "off":
            is_machine_on = False
        elif user_choice == "report":
            print_report()
            
        print("\n Thank you, enjoy your coffee and don't burn yourself!")


if __name__ == "__main__":
  run()