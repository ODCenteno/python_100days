import csv
import smtplib
import datetime as dt
import pandas as pd
from random import randint

FILES = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]


bddata = pd.read_csv("birthdays.csv")
print(bddata)

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
date = today.date()
month = today.month
day = today.day
print(day, month, date)

for num,bdday in enumerate(bddata["day"]):
    if day == bdday and month == bddata['month'][num]:
        print(f"Today is your birthday, congrats {bddata['name'][num]}\n")

        with open(f"./letter_templates/letter_{randint(1, 3)}.txt") as letter:
            content = letter.read()
            content = content.replace("[NAME]", f"{bddata['name'][num]}")
        print(content)
# 4. Send the letter generated in step 3 to that person's email address.

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=bddata['email'][num],
                msg=f"Subject:Happy Birthday {bddata['name'][num]}!\n\n{content}"
            )


