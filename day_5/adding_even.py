"""
## Adding Evens

# Instructions

You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

"""

def calc_total_even():

    total_even = sum(even for even in range(2, 101, 2))
    print(total_even)

if __name__ == '__main__':
    calc_total_even()