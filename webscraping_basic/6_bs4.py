# Python Web Scraping

# Title : BeautifulSoup4
# Date : 2020-08-13
# Creator : tunealog

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# Get elements from title
print(soup.title)

# Get elements from title (Only text)
print(soup.title.get_text())

# Get elements from "a" tag which meets first
print(soup.a)

# Get attributes from "a" tag which meets first
print(soup.a.attrs)

# Get specific attributes from "a" tag which meets first
print(soup.a["href"])

# Find elements from "a" tag which class="Nbtn_upload"
print(soup.find("a", attrs={"class": "Nbtn_upload"}))

# Find some element which class="Nbtn_upload"
print(soup.find(attrs={"class": "Nbtn_upload"}))

# Find elements from "a" tag which text="Some Text"
webtoon = soup.find("a", text="Some Text")
print(webtoon)

# "a" tag from found the results
rank1 = soup.find("li", attrs={"class": "rank01"})
print(rank1.a.get_text())

# next_sibling
print(rank1.next_sibling)
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank2.a.get_text())
print(rank3.a.get_text())

# previous_sibling
rank4 = rank2.previous_sibling.previous_sibling
print(rank4.a.get_text())

# parent
print(rank1.parent)

# find_next_sibling
rank5 = rank1.find_next_sibling("li")
print(rank5.a.get_text())

# find_previous_sibling
rank6 = rank3.find_previous_sibling("li")
print(rank6.a.get_text())

# find_next_siblings
print(rank1.find_next_siblings("li"))
