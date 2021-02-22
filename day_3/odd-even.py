"""
Creat a program that evaluates if a nuber is odd or even
"""

def main():
    number = int(input('Enter a number: '))
    check_number(number)


def check_number(number):
    if number % 2 == 0:
        print('It is even')
    else:
        print('It is odd')


def get_number():
    try:
        number = input('Enter a number: ')
        return number
    except:
        print('Only numbers please')

if __name__ == '__main__':
    main()