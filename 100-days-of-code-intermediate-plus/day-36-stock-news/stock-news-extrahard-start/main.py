import requests
import datetime as dt
import os
from dotenv import load_dotenv
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

load_dotenv('C:/Users/Dell/PycharmProjects/.env.txt')
STOCK_API_KEY = os.getenv('STOCK_API_KEY')

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").



sp_url = 'https://www.alphavantage.co/query'
stock_parameters = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'apikey': STOCK_API_KEY
}
sp_response = requests.get(sp_url, params=stock_parameters)
sp_data = sp_response.json()
sp_data_list = [value for (key, value) in sp_data.items()]

yesterday_date = str(dt.date.today() - dt.timedelta(days=2))
# print(f"Yesterday: {yesterday_date}")
two_days_ago_date = str(dt.date.today() - dt.timedelta(days=3))
# print(f"Two days ago: {two_days_ago_date}")

#Update dates
sp_two_days_ago_close = float(sp_data['Time Series (Daily)'][two_days_ago_date]['4. close'])
sp_yesterday_close = float(sp_data['Time Series (Daily)'][yesterday_date]['4. close'])
sp_delta_perc = round((sp_yesterday_close - sp_two_days_ago_close)/(sp_two_days_ago_close)*100,1)
# print(f"SP delta: {sp_delta_perc}%")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

news_url = 'https://newsapi.org/v2/everything'
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
news_keyword = "TSLA"

news_parameters = {
    'q': news_keyword,
    'apiKey': NEWS_API_KEY
}
news_response = requests.get(news_url, params=news_parameters)
news_data = news_response.json()
stock_news = [item for item in news_data['articles'][:3]]
compact_list = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in stock_news]
# print(stock_news)



## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

account_sid = ""
auth_token = ""
twilio_pn = ""
my_pn = ""

# if sp_delta_perc >= 5:
#     for x in range(0, 3):
#         client = Client(account_sid, auth_token)
#         message = client.messages \
#                         .create(
#                              body=f"{STOCK}: {sp_delta_perc}\n"
#                                 f"Headline: {stock_news[x]['title']}\n"
#                                 f"Brief: {stock_news[x]['description']}",
#                              from_=twilio_pn,
#                              to=my_pn
#                          )
#
#         print(message.status)

if sp_delta_perc >= 5:
    for x in range(0, 3):
        print(f"{STOCK}: {sp_delta_perc}%\n"
                f"Headline: {stock_news[x]['title']}\n"
                f"Brief: {stock_news[x]['description'][:100]}..."
              )
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

