# Python Web Scraping

# Title : BeautifulSoup4
# Date : 2020-08-20
# Creator : tunealog

import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=노트북&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class": re.compile("^search-product")})

for item in items:

    # Ignore Ad
    ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
    if ad_badge:
        print("<Ignore Ad>")
        continue

    name = item.find("div", attrs={"class": "name"}).get_text()

    # Ignore Apple
    if "Apple" in name:
        print("<Ignore Apple>")
        continue
    price = item.find("strong", attrs={"class": "price-value"}).get_text()

    # Rating
    rate = item.find("em", attrs={"class": "rating"})
    if rate:
        rate = rate.get_text()
    else:
        print("<Ignore none rating>")
        continue

    # Rating count
    rate_cnt = item.find(
        "span", attrs={"class": "rating-total-count"})
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
        rate_cnt = rate_cnt[1:-1]
    else:
        print("<Ignore none rating count>")
        continue

    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
        print(name, price, rate, rate_cnt)
