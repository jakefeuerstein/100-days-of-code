import requests
import datetime as dt

MY_LAT = 45.552158
MY_LONG = -73.882683

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# latitude = data['iss_position']['latitude']
# longitude = data['iss_position']['longitude']
#
# iss_position = (latitude, longitude)
#
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = dt.datetime.now()
print(time_now.hour)