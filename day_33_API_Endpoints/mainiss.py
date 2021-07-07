"""Exercise: Connect to the ISS API to get the current position coordinates and
use the Reverse Geocoding Convertor to see the ISS position on a map."""

import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 24.154712665484727
MY_LNG = -110.31514683456099
MY_EMAIL = "odcenteno.dev@gmail.com"
MY_PASS = "Odcenteno.dev()"

def run():
    """Main function that controls the proces to get the ISS cordenates and check if is night time, if does, then
    send an email to alert to look up
    """

    while True:
        time.sleep(60)
        iss_is_over = is_iss_overhead()
        if iss_is_over and is_night():
            send_email()

def is_iss_overhead():
    """Function that check if the ISS is in the closer sky coordinates. Return True"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_longitud = float(data["iss_position"]["longitude"])
    iss_latitud = float(data["iss_position"]["latitude"])
    iss_location = (iss_longitud, iss_latitud)
    print(f"iss_longitud: {iss_longitud}\niss_latitud: {iss_latitud}")

    # Reverse Geocoding Convert Lat Long to Address
    # https://www.latlong.net/Show-Latitude-Longitude.html

    if (MY_LAT - 1) <= iss_latitud <= (MY_LAT + 1) and (MY_LNG - 1) <= iss_longitud <= (MY_LNG + 1):
        print(f"The super duper ISS is over the sky, look up!")
        return True
    elif (MY_LAT - 5) <= iss_latitud <= (MY_LAT + 5) and (MY_LNG - 5) <= iss_longitud <= (MY_LNG + 5):
        print(f"The super duper ISS is near, wait for it!")
        return True
    else:
        print("No ISS in the sky at the moment.")


def is_night():
    """Function that check the time and if is night then return true"""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # print(data)

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 6
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    if sunset in range(0, 6):
        sunset = sunset + 18
    else:
        sunset = sunset - 6

    print(f"Sunrise hour: {sunrise}\nSunset hour: {sunset}")

    my_time = datetime.now().hour
    print(f"Current hour: {my_time}")

    if my_time >= sunset or my_time in range(0, sunrise):
        return True


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Look Up!, the ISS is passing over\n\nIt will take only a few seconds, enjoy!\n{datetime.time()}"
        )


if __name__ == "__main__":
    run()
