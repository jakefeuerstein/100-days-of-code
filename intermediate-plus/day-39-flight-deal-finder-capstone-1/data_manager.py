import requests

USERNAME = ""
URL = ""
TOKEN = ""

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.headers = {'Authorization': TOKEN}

    # TODO get and store cities and min prices from G

    def get_info(self):
        self.response = requests.get(URL, headers=self.headers).json()
        return self.response

#TODO put IATAs

    def put_iata(self, row: int, iata: str):
        put_url = f"{URL}/{row}"
        params = {
            'price': {
                'iataCode': iata
            }
        }
        result = requests.put(put_url, headers=self.headers, json=params)
        print(result.text)

#TODO transfer cities and min prices to main