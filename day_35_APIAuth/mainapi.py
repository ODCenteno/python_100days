"""Main Python file for the 35th codding day"""

import requests


API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
params = {
    "lat": 24.159734,
    "lon": -110.319012,
    "units": "metric",
    "appid": "cd3c3d5e6757ca22d3c3e2a35a9f25df",
}

response = requests.get(API_ENDPOINT, params=params)
response.raise_for_status()
status = response.status_code
print(f"Status: {status}")
response = response.json()

print(response)

print(f"Current temp: {response['hourly']}")
