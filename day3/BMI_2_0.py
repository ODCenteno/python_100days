"""
Instructions
Write a program that interprets the body mass index (BMI) based on a user's weight and heigth.

It should tell them the interpretation of their BMI based on the BMI value.

- Under 18.5 they are underweight
- Over 18.5 but below 25 they have a normal weight
- Over 25 but below 30 they are overweight
- Over 30 but below 35 they are obese
- Above 35 they are clinically obese.
"""

def main():
    height = get_height()
    weight = get_weight()
    bmi = calc_bmi(height, weight)

    if bmi < 18.5:
        print(f'Your BMI is {bmi}, you are underweight')
    elif bmi < 25:
        print(f'Your BMI is {bmi}, you have a normal weight')
    elif bmi < 30:
        print(f'Your BMI is {bmi}, you are overweight')
    elif bmi < 35:
        print(f'Your BMI is {bmi}, you are obese')
    else:
        print(f'Your BMI is {bmi}, you are clinically obese')
    

def get_height():
    height = int(input('Please enter your heigh(in): '))
    return height

def get_weight():
    weight = int(input('Please enter your weigh(lb): '))
    return weight

def calc_bmi(height, weight):

    bmi = (weight / (height**2))*703
    return round(bmi)

if __name__ == '__main__':
    main()