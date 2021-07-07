"""Exercise: Connect to the Sunse Sunraise API to get the current sunset and sunrise hours for my location"""

import requests
from datetime import datetime

MY_LAT = 24.154712665484727
MY_LNG = -110.31514683456099

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 6
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 18

print(sunrise, sunset)

my_time = datetime.now().hour
print(my_time)
