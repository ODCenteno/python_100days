"""
 Average Height

# Instructions

You are going to write a program that calculates the average student height from a List of heights. 

e.g. `student_heights = [180, 124, 165, 173, 189, 169, 146]`

The average height can be calculated by adding all the heights together and dividing by the total number of heights. 

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = **1146**

There are a total of **7** heights in `student_heights`

1146 ÷ 7 = **163.71428571428572**

Average height rounded to the nearest whole number = **164**

**Important** You should not use the `sum()` or `len()` functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

# Example Input 

```
156 178 165 171 187
```
"""


def get_heights():
    
    heights = input(f'Welcome to the average height calculator\nTo start please enter the heights separated by a space:\nType heights: ').strip().split(' ')
    heights = [int(height) for height in heights]
    print(f'The heights are: {heights}')

    return heights

def average_heights(heights):
    
    count = 0
    suma = 0

    for height in heights:
        count += 1
        suma += height
    
    average = round(suma / count)
    print(f'The average height is: {average}')

if __name__ == '__main__':
    students_heights = get_heights()
    average_heights(students_heights)