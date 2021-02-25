"""
## Area Calc

# Instructions

You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height ✖️ wall width) ÷ coverage per can. 

e.g. Height = 2, Width = 4, Coverage = 5

number of cans = (2 ✖️ 4) ÷ 5 

                         = 1.6

But because you can't buy 0.6 of a can of paint, the **result should be rounded up** to **2** cans. 

IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.

# Example Input

test_h = 3
test_w = 9

# Example Output
You'll need 6 cans of paint.

"""
import math

def welcome():
    print(f'''\nWELCOME!\n\n This is a calc tool to estimate the paint cans needed to paint a wall\n
    To do so, we need the dimensions of the wall in meters.\n\n''')

def get_height():
    height = float(input(f'Enter the height of the wall (only the value in meters):'))
    return height

def get_width():
    width = float(input(f'Enter the width of the wall (only the value in meters):'))
    return width

def area_calc(height, width):
    coverage = 5        # The area that each can actually paint
    number_of_cans = ((height * width) / coverage)
    print(f'Number of cans: {number_of_cans}')
    print(f'The number of cans needed are: {math.ceil(number_of_cans)}')  # Ceil: round up a number

if __name__ == '__main__':
    welcome()
    height = get_height()
    width = get_width()
    area_calc(height, width)