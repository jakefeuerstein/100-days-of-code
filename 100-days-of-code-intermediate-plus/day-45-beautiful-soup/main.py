from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

# print(type(yc_web_page))

soup = BeautifulSoup(yc_web_page, "html.parser")
#
articles = soup.find_all(name="span", class_="titleline")
print(type(articles))
# article_text = []
# article_links = []
# for article_tag in articles:
#     text = article_tag.getText()
#     article_text.append(text)
#     link = article_tag.find(name="a").get("href")
#     article_links.append(link)
#
# article_upvotes = [int(upvotes.getText().split(" ")[0]) for upvotes in soup.find_all(name="span", class_="score")]
#
# high_upvotes = max(article_upvotes)
# high_index = article_upvotes.index(high_upvotes)
# print(article_text[high_index])
# print(article_links[high_index])
# print(article_upvotes[high_index])







# import lxml

# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# soup.title.string
# soup.title.name
# soup.a
#
# # print(soup.prettify())
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
# # for tag in all_anchor_tags:
# #     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# name = soup.select_one(selector="#name")
#
#
#
