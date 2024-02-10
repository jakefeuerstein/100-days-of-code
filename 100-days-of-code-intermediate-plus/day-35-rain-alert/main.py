import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv  # pip install python-dotenv

print(os.environ.get('SOME_VAR'))

load_dotenv("")
WA_API_KEY = os.getenv("WA_API_KEY")

print(WA_API_KEY)

WA_KEY_0 = ""

WA_Endpoint = "https://api.weatherapi.com/v1/forecast.json"
parameters = {
    'key': os.environ.get('WA_API_KEY'),
    'q': "44405"
}

account_sid = ""
auth_token = ""
twilio_pn = ""
my_pn = ""


response = requests.get(WA_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data['forecast']['forecastday'][0]['hour'][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data['condition']['code']
    if int(condition_code) > 1030:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                         body="Bring an umbrella. ☂️",
                         from_=twilio_pn,
                         to=my_pn
                     )

    print(message.status)



