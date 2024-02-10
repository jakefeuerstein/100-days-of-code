import requests

URL = "https://api.tequila.kiwi.com/"
API_KEY = ""
headers = {
    'apikey': API_KEY
}

def get_cheapest_flight():
    search_url = URL + "search/"
    params = {
        'fly_from': "LON",
        'fly_to': "PAR",
        'date_from': "01/09/2023",
        'date_to': "07/09/2023",
        'limit': 100
    }
    response = requests.get(search_url, params=params, headers=headers)
    response.raise_for_status()
    data = response.json()
    price = data['data'][0]['price']
    print(price)
    return price


get_cheapest_flight()