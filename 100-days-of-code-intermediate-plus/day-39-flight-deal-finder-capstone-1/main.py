import datetime as dt
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData

ORIGIN = "LON"

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# ------------APIs----------

# Google Sheet Data Management - https://sheety.co/
    # enable PUT

# Kiwi Partners Flight Search API (Free Signup, Requires Credit Card Details) - https://partners.kiwi.com/
    # account: first name / last name
    # product type: Meta search, one-way and return
    # partnership: "Book with Kiwi.com" or the affiliate program

# Tequila Flight Search API Documentation - https://tequila.kiwi.com/portal/docs/tequila_api
#
# Twilio SMS API - https://www.twilio.com/docs/sms

#get and put IATAs

data_manager = DataManager()

sheet_data = data_manager.get_info()['prices']

flight_search = FlightSearch()



def check_for_iata():
    global has_iata = False
    for row in sheet_data:
        if sheet_data[row]['iataCode'] == "":
            has_iata = False
            break
        else:
            has_iata = True

def add_iata()
    for row in sheet_data:
        row_id = row['id']
        iata = flight_search.get_iata(row['city'])
        sheet_data.put_iata(row_id, iata)

#TODO add search date range

search_start_date = (dt.date.today() + dt.timedelta(days=1)).strftime("%m/%d/%Y")
search_end_date = (dt.date.today() + dt.timedelta(days=183)).strftime("%m/%d/%Y")


#TODO compare lowest prices (data_manager) to min price (G)

flight_data = FlightData()


for row in travel_specs_info:
    flights = flight_search.get_flights(ORIGIN, row['iataCode'], search_start_date, search_end_date)
    if flights['data'][0]['price'] <= travel_specs_info['lowestPrice']:
        date = flights['data'][0]['utc_arrival']
        month = date.slice(2)
        day = date.slice(2, 4)
        year = date.slice(4, 8)
        flight_data()

#TODO if actionable, send message (notif_mgr)

