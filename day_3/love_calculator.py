"""
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:
"Your score is **z**."
"""

def true_love():

    name1 = input('What is your name?: ').lower()
    name2 = input('What is their name?: ').lower()

    full_name = name1 + name2

    true_number = str(count_true(full_name))
    love_number = str(count_love(full_name))

    score = true_number + love_number
    print(score)
    result(int(score))

def count_true(full_name):

    count_true = str(sum(['true'.count(x) for x in full_name]))
    print(f'The total count for true is {count_true}')
    return count_true


def count_love(full_name):
    count_love = str(sum(['love'.count(x) for x in full_name]))
    print(f'The total count for true is {count_love}')
    return count_love


def result(score):
    if score < 10 or score > 90:
        print(f"Your score is {score}, you go together like coke and mentos.")
    elif score >= 40 and score <= 50:
        print(f"Your score is {score}, you are alright together.")
    else:
        print(f"Your score is {score}.") 

if __name__ == '__main__':
    print(f'\nWelcome to Love Calculator\n\n')
    true_love()