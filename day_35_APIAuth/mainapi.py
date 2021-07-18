"""Main Python file for the 35th codding day. Using the Open Weather API"""

import os
import requests
from twilio.rest import Client

from keys import keys

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
OWM_API_key = keys["OWM_API_key"]
params = {
    "lat": 29.951065,
    "lon": -90.071533,
    "units": "metric",
    "appid": OWM_API_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(API_ENDPOINT, params=params)
response.raise_for_status()
status = response.status_code
print(f"Status: {status}")
response = response.json()

print(f"The response is: {response}")

print(f"Current temp: {response['hourly'][0]['temp']}")
print(f"Current weather: {response['hourly'][0]['weather'][0]}")
print(f"Current id and description:\nid: {response['hourly'][0]['weather'][0]['id']}\ndescription: {response['hourly'][0]['weather'][0]['description']}")

weather_slice = response['hourly'][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today though ☔️",
        from_='+16159916129',
        to='+525574017790',
    )

    print(message.status)


for temp in range(0, 12):
    print(f"The next {temp + 1} hours:{response['hourly'][temp]['temp']}ºC tempeture.")
