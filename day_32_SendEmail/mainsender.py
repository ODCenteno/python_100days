import smtplib
import datetime as dt
from random import choice

my_email = "odcenteno.dev@gmail.com"
password = "Odcenteno.dev()"


def run():
    """The main function get the current day of the week, get a quote and send email"""
    date = get_date()
    if date == 3:
        quote = get_quote()
        print(quote)
        send_email(quote)

def get_date():
    """Return the day of the week using datetime module now.weekday() where monday = 0"""
    now = dt.datetime.now()
    weekday = now.weekday()
    print(f"today is: {weekday}")
    return weekday

def get_quote():

    with open("quotes.txt", "r", encoding="utf-8") as file:
        readfile = file.readlines()
        quote_list = [line.strip() for line in readfile]
        print(quote_list)
        today_quote = choice(quote_list)
        return today_quote

def send_email(quote):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="daniel.centeno.manzo@gmail.com",
            msg=f"Subject:Your weekly inspirational quote\n\n{quote}"
        )


if __name__ == "__main__":
    run()
