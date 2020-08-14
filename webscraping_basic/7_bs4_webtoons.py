# Python Web Scraping

# Title : BeautifulSoup4
# Date : 2020-08-15
# Creator : tunealog

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# To scrap which Naver Webtoons list
cartoons = soup.find_all("a", attrs={"class": "title"})

# Return which class=title in all "a" element
for cartoon in cartoons:
    print(cartoon.get_text())
