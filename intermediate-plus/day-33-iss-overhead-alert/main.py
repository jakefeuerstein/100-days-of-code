import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 3
MY_LONG = 168

GMAIL = "_@gmail"
PASSWORD =""


def within_pos():
    within_lat = False
    within_long = False
    if iss_latitude <= MY_LAT + 5 and iss_latitude >= MY_LAT - 5:
        within_lat = True
    if iss_longitude <= MY_LONG + 5 and iss_longitude >= MY_LONG - 5:
        within_long = True
    if within_lat and within_long:
        return True
    else:
        return False

def is_dark():

    if current_hour <= sunrise or current_hour >= sunset:
        return True
    else:
        return False

def send_email():
    with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
        connection.starttls()
        connection.login(user=GMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=GMAIL,
            to_addrs=GMAIL,
            msg=f"Subject:Look up for ISS"
        )

def run_program():
    if within_pos() and is_dark():
        send_email()
    time.sleep(60)
    run_program()

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
current_hour = time_now.hour
current_minute = time_now.minute
recorded_minute = 61


print(type(current_hour))
run_program()


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



