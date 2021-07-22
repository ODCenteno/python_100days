import requests
from keys import keys
from twilio.rest import Client

NEWS_API_KEY = keys["NEWS_API_KEY"]
STOCK_API_ALPHAVANTAGE = keys["STOCK_API_ALPHAVANTAGE"]
TWILIO_ACC_ID = keys["TWILIO_ACC_ID"]
TWILIO_API_KEY = keys["TWILIO_API_KEY"]
TWILIO_number = keys["TWILIO_number"]

# STOCK_API_ALPHAVANTAGE_KEY = os.environ.get("$STOCK_API_ALPHAVANTAGE")
# NEWS_API_KEY = os.environ.get(f"NEWS_API_KEY")

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_params = {
    "qInTitle": COMPANY_NAME,
    "from": "2021-07-15",
    "to": "2021-07-21",
    "apiKey": NEWS_API_KEY,
}
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": COMPANY_NAME,
    "apikey": STOCK_API_ALPHAVANTAGE,
}


def get_news():
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
    return news_data


def stock_request():
    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]
    return data


stock_data = stock_request()
stock_closing_prices = [values["4. close"] for (key, values) in stock_data.items()]

# getting closing prices for yesterday and the day before yesterday

yesterday_closing_price = float(stock_closing_prices[0])
day_before_yesterday_closing_price = float(stock_closing_prices[1])
print(f"{yesterday_closing_price}\n{day_before_yesterday_closing_price}")

# Calculate the percentage difference
price_difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)
diff_percent = (price_difference / yesterday_closing_price) * 100
print(f"diff_percent: {diff_percent}")

if diff_percent > 0.5:
    news_articles = get_news()
    three_articles = news_articles[:3]
    print(three_articles)
