import datetime
from keys import keys
import requests
from twilio.rest import Client

NEWS_API_KEY = keys["NEWS_API_KEY"]
STOCK_API_ALPHAVANTAGE = keys["STOCK_API_ALPHAVANTAGE"]
TWILIO_ACC_ID = keys["TWILIO_ACC_ID"]
TWILIO_API_KEY = keys["TWILIO_API_KEY"]
TWILIO_number = keys["TWILIO_number"]

# STOCK_API_ALPHAVANTAGE_KEY = os.environ.get("$STOCK_API_ALPHAVANTAGE")
# NEWS_API_KEY = os.environ.get(f"NEWS_API_KEY")

STOCK = "AAPL"
COMPANY_NAME = "Apple Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_params = {
    "qInTitle": "Tesla",
    "from": "2021-06-30",
    "to": "2021-07-20",
    "apiKey": NEWS_API_KEY,
}
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "outputsize": "compact",
    "apikey": STOCK_API_ALPHAVANTAGE,
}
## ✅ STEP 1: Use https://www.alphavantage.co/query
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
status = response.status_code
stock_data = response.json()
print(f"Stock response:\n\n {stock_data}\n\n")

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: ✅Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: ✅ Work out the value of 5% of yesterday's closing stock price.

# Get the date for yesterday an two days ago using datetime module
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
two_days_ago = today - datetime.timedelta(days=2)

# Using the dates got before and the stock data to obtain the stock closed price for each day
stock_time_series = stock_data["Time Series (Daily)"]
yesterday_stock_close = float(stock_time_series[f"{yesterday}"]["4. close"])
two_days_stock_close = float(stock_time_series[f"{two_days_ago}"]["4. close"])
print(f"Yesterday Close: {yesterday_stock_close}\nTwo Days Close: {two_days_stock_close}\n\n")

# Make the maths to calculate the difference between the daily closing stock price
daily_close_substraction = abs(round(yesterday_stock_close, 2) - round(two_days_stock_close, 2))


# Calculate the Stock price close percentage change for the two day before the actual date
daily_stock_ratio = round(((daily_close_substraction * 100) / yesterday_stock_close), 3)
print(f"Stock price close daily ratio: {daily_stock_ratio} %\n\n")

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
response = requests.get(NEWS_ENDPOINT, params=news_params)
response.raise_for_status()
status = response.status_code
news_data = response.json()
news_data = news_data["articles"]
print(f"\nNews Data: {news_data}\n")

get_articles_content = [{"title": news_data[num]["title"], "description": news_data[num]["description"]} for num in range(3)]
print(f"\nList with dictionaries of titles and descriptions:\n{get_articles_content}\n")

# Printing Titles:


def print_news(get_articles_title, daily_stock_ratio):

    for i in range(len(get_articles_title)):
        return (f"TSLA: {daily_stock_ratio}\nHeadline: {get_articles_title[i]['title']}:\nBrief: {get_articles_title[i]['description']}\n")



## STEP 3: Use twilio.com/docs/sms/quickstart/python
account_sid = TWILIO_ACC_ID
auth_token = TWILIO_API_KEY
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=f"{print_news(get_articles_content, daily_stock_ratio)}",
                     from_='+16159916129',
                     to='+525574017790',
                 )

print(message.sid)

# Send a separate message with each article's title and description to your phone number.
#HINT 1: Consider using a List Comprehension.
#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

