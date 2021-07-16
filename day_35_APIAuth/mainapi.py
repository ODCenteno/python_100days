"""Main Python file for the 35th codding day. Using the Open Weather API"""

import requests


API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
params = {
    "lat": 18.229412,
    "lon": -94.893153,
    "units": "metric",
    "appid": "cd3c3d5e6757ca22d3c3e2a35a9f25df",
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
    print("Bring and umbrella")


for temp in range(0, 12):
    print(f"The next {temp + 1} hours:{response['hourly'][temp]['temp']}ºC tempeture.")
