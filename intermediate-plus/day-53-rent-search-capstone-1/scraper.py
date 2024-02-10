# Use BeautifulSoup/Requests to scrape all the listings from the Zillow web address (Step 4 above).
#   Create a list of links for all the listings you scraped. e.g.
#   Create a list of prices for all the listings you scraped. e.g.
#   Create a list of addresses for all the listings you scraped. e.g.

import requests
from bs4 import BeautifulSoup
from pprint import pprint

ZILLOW_BASE_URL = "https://www.zillow.com/homes/for_rent/"
ZILLOW_END_URL = "?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22" \
             "%3A%7B%22west%22%3A-122.63417281103516%2C%22east%22%3A-122.23248518896484%2C%22south%22%3A37" \
             ".66639245996975%2C%22north%22%3A37.88403027709227%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue" \
             "%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C" \
             "%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22" \
             "%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22" \
             "%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22" \
             "%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
headers = {
    'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
        "application/signed-exchange;v=b3;q=0.9",
    'Accept-Encoding':"gzip, deflate",
    'Accept-Language': "en-US,en;q=0.9",
    'Connection':"keep-alive",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 " \
                 "Safari/537.36"
}

SEARCH_LIMIT = 100
HITS_PER_PAGE = 42

class Scraper():
    def scrape(self):
        num_pages = SEARCH_LIMIT//HITS_PER_PAGE
        zillow_complete_url = ZILLOW_BASE_URL+"/"
        response = requests.get(ZILLOW_BASE_URL+ZILLOW_END_URL, headers=headers)
        response.raise_for_status()
        html = response.content
        soup = BeautifulSoup(html, "html.parser")

        if num_pages > 1:
            page_num = 1
            for i in range(num_pages):
                response = requests.get(ZILLOW_BASE_URL+str(page_num)+"/"+ZILLOW_END_URL, headers=headers)
                response.raise_for_status()
                html = response.content
                new_soup = BeautifulSoup(html, "html.parser")
                soup.append(new_soup)
                page_num += 1

        listings = soup.select('li[class*="ListItem"]')
        # print(listings[2].find('address') is not None)
        listing_data = []
        for listing in listings:
            if listing.find('address') is not None:
                address = listing.find('address').getText()
            else:
                address = "No address"
            if listing.find('span') is not None:
                price = listing.find('span').getText()
            else:
                price = "No price"
            if listing.find('a') is not None:
                link = listing.select_one('a[class*="StyledProperty"]').get('href')
            else:
                link = "No link"
            dict = {'address': address,
                    'price': price,
                    'link': link
                    }
            listing_data.append(dict)
        listing_data = listing_data[:2]
        # pprint(listing_data)
        return listing_data
