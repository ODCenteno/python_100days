from logo import logo
import os


#Add
def add(n1, n2):
    return n1 + n2

#Substract
def substract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide,
}

def calculator():
    try:
        num1 = float(input("What's the first number?: "))
    except ValueError:
        calculator()
    
    for symbol in operations:
        print(symbol)

    should_continue = True 

    while should_continue:
        operation_symbol = input("pick an operation from the list above: ")

        num2 = float(input("What's the second number?: "))
        # if num2 is not type(float) or num2 is not type(int):
        #     print('That is not a valid number')
        #     num2 = float(input("What's the second number?: "))

        calculation_function = operations[operation_symbol]
        result = calculation_function(num1, num2)
        print(f'{num1} {operation_symbol} {num2} = {result}')

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == 'y':
            num1 = result
        else:
            should_continue = False
            os.system('clear')
            calculator()


if __name__ == '__main__':
    print(logo)
    calculator()