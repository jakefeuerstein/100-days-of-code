import requests
import datetime as dt
import math

#Nutritionix constants
APP_ID = ""
API_KEY = ""
NUTRITIONIX_EP = "https://trackapi.nutritionix.com/v2/natural/exercise"



headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

exercise_input = input("What exercise did you do today?")
# exercise_input = "ran 1 mile"

parameters = {
    'query': exercise_input
}

nut_response = requests.post(url=NUTRITIONIX_EP, headers=headers, json=parameters)
result = nut_response.json()

# exercise = result['exercises'][0]['name']
# duration = math.floor(result['exercises'][0]['duration_min'])
# calories = result['exercises'][0]['nf_calories']

# print(exercise)
# print(duration)
# print(calories)

#Sheety

SHEETY_USERNAME = ""
sheety_project_name = "workoutTracking"
sheety_sheet_name = "sheet1"
sheety_code = ""
sheety_auth = ""
# SHEETY_EP = f"https://api.sheety.co/{sheety_code}/{SHEETY_USERNAME}/{sheety_project_name}/{sheety_sheet_name}"
SHEETY_EP = ""
# print(SHEETY_EP)

date = dt.datetime.now().strftime("%Y/%m/%d")
time = dt.datetime.now().strftime("%H:%M:%S")

sheety_headers = {'Authorization': f"Bearer {sheety_auth}"}

for exercise in result['exercises']:
    sheety_params = {
        sheety_sheet_name: {
            'date': date,
            'time': time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }

    }
    sheety_response = requests.post(SHEETY_EP, json=sheety_params, headers=sheety_headers)

# sheety_response = requests.get(url=SHEETY_EP)
print(sheety_response.text)