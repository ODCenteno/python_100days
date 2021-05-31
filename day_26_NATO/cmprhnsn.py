from random import randint
#
#
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# squared_numbers = [n*n for n in numbers]
#
# print(squared_numbers)
#
# with open('file1.txt') as file1:
#     list1 = file1.read().splitlines()
#
#
# with open('file2.txt') as file2:
#     list2 = file2.read().splitlines()
#
# result = [int(num) for num in list1 if num in list2]
# print(result)

# students = ['Carlitos', 'Lucy', 'Michael', 'Frank', 'Lupita', 'Camila']
#
# students_scores = {student: randint(1, 100) for student in students}
# print(students_scores)
# passed_students = {student: value for (student, value) in dict.items(students_scores) if value >= 60}
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# sentence = sentence.replace("?", "")
# result = {word: len(word) for word in list(sentence.split(" "))}
# print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)