import requests
import datetime as dt

USERNAME = "jfire"
TOKEN = ""
GRAPH_ID = "graph1"

pixela_ep = "https://pixe.la/v1/users"

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': "yes",
    'notMinor': "yes"
}

# response = requests.post(url=pixela_ep, json=user_params)
# print(response.text)

graph_ep = f"{pixela_ep}/{USERNAME}/graphs"

graph_config = {
    'id': "graph1",
    'name': "Cycling Graph",
    'unit': "Km",
    'type': "float",
    'color': "ajisai"
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_ep, json=graph_config, headers=headers)
# print(response.text)

today = dt.datetime(year=2023, month=1, day=1).strftime("%Y%m%d")

pixel_params = {
    'date': today,
    'quantity': "1"
}

pixel_ep = f"{graph_ep}/{GRAPH_ID}"

# response = requests.post(url=pixel_ep, json=pixel_params, headers=headers)
# print(response.text)

pixel_put_ep = f"{pixel_ep}/{today}"

# response = requests.put(url=pixel_put_ep, json={'quantity': "2"}, headers=headers)
# print(response.text)

response = requests.delete(url=pixel_put_ep, headers=headers)
print(response.text)