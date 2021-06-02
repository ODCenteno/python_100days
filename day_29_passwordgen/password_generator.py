"""Password Generator Algorithm"""

import random

def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letters = [random.choice(letters) for letter in range(random.randint(8, 10))]
    random_symbols = [random.choice(symbols) for symbol in range(random.randint(2, 4))]
    random_numbers = [random.choice(numbers) for number in range(random.randint(2, 4))]

    password_list = random_letters + random_numbers + random_symbols
    random.shuffle(password_list)

    password = ''.join(password_list)
    print(f'Your password is: {password}')
    return password
