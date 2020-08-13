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

# "a" tag from found the results
rank1 = soup.find("li", attrs={"class": "rank01"})
print(rank1.a)
