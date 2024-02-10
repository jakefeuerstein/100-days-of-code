import requests

URL = "https://api.tequila.kiwi.com/"
API_KEY = ""
headers = {
    'apikey': API_KEY
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    # TODO transfer city/IATA (data_manager),
    def get_iata(self, city):
        iata_url = URL + "locations/query"

        params = {
            'term': city
        }

        response = requests.get(url=iata_url, headers=headers, params=params).json()
        iata = response['locations'][0]['code']
        return iata

    #TODO search date range (main)

    def get_flights(self, fly_from, fly_to, date_from, date_to):
        search_url = URL + "/search"
        params = {
            # 'fly_from': fly_from,
            # 'fly_to': fly_to,
            # 'date_from': date_from,
            # 'date_to': date_to,
            # 'limit': 1
            'fly_from': "LON",
            'fly_to': "PAR",
            'date_from': "01/09/2023",
            'date_to': "07/09/2023",
            'limit': 100
        }
        response = requests.get(search_url, params=params, headers=headers).json()
        data = response['data']
        return data


    #TODO get city/IATA, price, dates
