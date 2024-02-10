import requests
import pprint
from bs4 import BeautifulSoup
from urllib.request import urlopen
import codecs

# URL = "https://www.empireonline.com/movies/features/best-movies-2/"
# URL = "https://news.ycombinator.com/news?p=4"
URL = "https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/"

# text = str(urlopen(URL).read())

response = requests.get(URL)
text = response.text

# print(text)

soup = BeautifulSoup(text, "html.parser")

#
initial_list_data = soup.find_all(name= "h3", class_="title")
# class_="jsx-4245974604"

print(initial_list_data)

# pprint.pprint(initial_list)
#
# final_list = initial_list.reverse()



# for movie in final_list:
#     file = open("movies.txt", 'w')
#     file.write(movie)