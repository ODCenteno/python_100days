"""
## Highest Score

# Instructions

You are going to write a program that calculates the highest score from a List of scores. 

e.g. `student_scores = [78, 65, 89, 86, 55, 91, 64, 89]`

**Important** you are not allowed to use the max or min functions. The output words must match the example. i.e 

> `The highest score in the class is: x`

# Example Input 

```
78 65 89 86 55 91 64 89
```

In this case, student_scores would be a list that looks like: `[78, 65, 89, 86, 55, 91, 64, 89]`

# Example Output 

```
The highest score in the class is: 91
```
"""

def eval_scores(scores):

    max_score = 0

    for score in scores:
        if score > max_score:
            max_score = score

    print(f'The highest score in the class is: {max_score}')

def get_scores():

    scores = input(f'Welcome to the max score calculator\nTo start please enter the scores separated by a space:\nType scores: ').strip().split(' ')
    scores = [int(score) for score in scores]

    return scores

if __name__ == '__main__':
    scores = get_scores()
    eval_scores(scores)