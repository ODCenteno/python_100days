"""Exercise: Connect to the ISS API to get the current position coordinates and
use the Reverse Geocoding Convertor to see the ISS position on a map."""

import requests


def run():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    longitud = data["iss_position"]["longitude"]
    latitud = data["iss_position"]["latitude"]
    iss_location = (longitud, latitud)
    print(f"longitud: {longitud}\nlatitud: {latitud}")

# Reverse Geocoding Convert Lat Long to Address
# https://www.latlong.net/Show-Latitude-Longitude.html


if __name__ == "__main__":
    run()
