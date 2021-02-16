""" 
Create a program to decide if someone coul ride a rollercoaster, depending of the height that must be over 120 cm to ride. Aditional to this, the age it's also needed to be checked to let the people pass, over 18 they can ride.

Aditional to this, we need to ask if the client want to take a photo of the ride, if they want it we need to charge $3 extra.
"""

def main():
    height = check_height()
    price = check_age(height)
    ticket_price(price)


def ticket_price(price):
    want_pic = input('Would you like to get a picture? [Y/N]: ').upper()

    if want_pic == 'Y':
        final_ticket_price = price + 3
        print(f'Ok kiddo, ride on and pay ${final_ticket_price}!\n')
    elif price == 0 and want_pic == 'N':
        print(f'Enjoy the ride!')
    else:
        print(f'Ok kiddo, ride on and pay ${price}!\n')


def check_age(height):
    if height:
        try:
            age = int(input('What is your Age: '))
        except TypeError:
            print('Try with numbers only')
            check_age()
        if age < 12:
            return 5
        elif age < 18:
            return 7
        elif age >= 45 and age <= 55:
            print(f'Everithing is going to be ok. Have a free ride on us')
            return 0
        else:
            return 12


def check_height():
    print('Welcome to the rollercoaster\n')

    try:
        height = int(input('Enter your height in cm: '))

        if height >= 120:
            height = True
            print('You are hight enough')
            return height
        else:
            return print('Sorry kiddo, you must be a little heighter to ride')
    except TypeError:
        print('Try with a number')
        main()

if __name__ == '__main__':
    main()


