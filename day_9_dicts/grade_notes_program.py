"""
## Grading Program

# Instructions

You have access to a database of `student_scores` in the format of a dictionary. The **keys** in `student_scores` are the **names** of the students and the **values** are their exam **scores**. 

Write a program that **converts their scores to grades**. By the end of your program, you should have a new dictionary called `student_grades` that should contain student **names** for **keys** and their **grades** for **values**. T**he final version** of the `student_grades` dictionary will be checked. 

**DO NOT** write any print statements.

This is the scoring criteria:

> Scores 91 - 100: Grade = "Outstanding"

> Scores 81 - 90: Grade = "Exceeds Expectations"

> Scores 71 - 80: Grade = "Acceptable"

> Scores 70 or lower: Grade = "Fail"

# Expected Output
'{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'
"""

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

def score_gradier(student_scores):
    student_grades = {}
    for key, val in student_scores.items():
        if val > 90:
            student_grades[key] = "Outstanding"
        elif val > 80:
            student_grades[key] = "Exceeds Expectations"
        elif val >70:
            student_grades[key] = "Acceptable"
        else:
            student_grades[key] = "Fail"
    return student_grades


if __name__ == '__main__':
    student_grades = score_gradier(student_scores)
    print(student_grades)