"""
## Prime Numbers

# Instructions

Prime numbers are numbers that can only be cleanly divided by itself and 1. 

[https://en.wikipedia.org/wiki/Prime_number](https://en.wikipedia.org/wiki/Prime_number)


**You need to write a function** that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

 
 ![](https://cdn.fs.teachablecdn.com/s0gceS97QD6MP5RUT49H)

Here are the numbers up to 100, prime numbers are highlighted in yellow:

![](https://cdn.fs.teachablecdn.com/NZqVclSt2qAe8KhTsUtw)

# Example Input 1
73

# Example Output 1
It's a prime number.
"""

# def check_user_prime(number):

#     if number == 2:
#         print(f'It\'s a prime number')
#     elif number > 1 and number % 2 == 0:
#         print(f'It\'s not prime')
#     elif number > 1 and number % 5 == 0:
#         print(f'It\'s not prime')
#     else:
#         print(f'It\'s a prime number')

def check_prime(number):
    number_is_prime = False

    if number == 2:
        number_is_prime = True
        return number_is_prime
    elif number == 5:
        number_is_prime = True
        return number_is_prime
    elif number > 1 and number % 2 == 0:
        return number_is_prime
    elif number > 1 and number % 3 == 0:
        return number_is_prime
    elif number > 1 and number % 5 == 0:
        return number_is_prime
    elif number > 1 and number % 7 == 0:
        return number_is_prime
    elif number > 1 and number % 9 == 0:
        return number_is_prime
    else:
        number_is_prime = True
        return number_is_prime

def number_range_checker(max_n):
    primes = []

    for i in range(2, max_n + 1):
        number_is_prime = check_prime(i)
        if number_is_prime:
            primes.append(i)
        else:
            continue
    if max_n == primes[-1]:
        print(f"Number {max_n} it is prime.")
    else:
        print(f"Number {max_n} it is not prime.")
    print(f'The total prime numbers up to {max_n} are: {primes}')



if __name__ == '__main__':
    n = int(input(f'Enter a positive number:'))
    #check_prime(number = n)
    number_range_checker(max_n = n)