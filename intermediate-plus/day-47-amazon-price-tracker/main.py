import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/..."
GMAIL = "...@gmail.com"
PW = ""

#------------------------------Get Amazon Data------------------------------------

headers = {'User-Agent': 'Mozilla 5.0',
           'Accept-Language': "English"}
response = requests.get(URL, headers=headers)
response.raise_for_status()
data = response.text
# print(data)

#------------------------------Soupify------------------------------------

soup = BeautifulSoup(data, "lxml")
price = int(soup.find(name="span", class_="a-price-whole").getText().split(".")[0])
# print(price)

#------------------------------Compare------------------------------------

price_limit = 13
if price < price_limit:
    print("Step 3")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=GMAIL, password=PW)
        connection.sendmail(
            from_addr=GMAIL,
            to_addrs=GMAIL,
            msg=f"Subject:Buy the Hammer!"
                f"\n\nIt's time to buy that hammer: {URL}"
        )


