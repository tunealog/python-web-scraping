# Python Web Scraping

# Title : BeautifulSoup4
# Date : 2020-08-23
# Creator : tunealog

import requests
import re
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15"}
for i in range(1, 6):
    url = "https://www.coupang.com/np/search?q=노트북&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(
        i)
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class": re.compile("^search-product")})

    for item in items:

        # Ignore Ad
        ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
        if ad_badge:
            continue

        name = item.find("div", attrs={"class": "name"}).get_text()

        # Ignore Apple
        if "Apple" in name:
            continue
        price = item.find("strong", attrs={"class": "price-value"}).get_text()

        # Rating
        rate = item.find("em", attrs={"class": "rating"})
        if rate:
            rate = rate.get_text()
        else:
            continue

        # Rating count
        rate_cnt = item.find(
            "span", attrs={"class": "rating-total-count"})
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()[1:-1]
        else:
            continue

        link = item.find("a", attrs={"class": "search-product-link"})["href"]

        if float(rate) >= 4.5 and int(rate_cnt) >= 100:
            print(f"Name : {name}")
            print(f"Price : {price}")
            print(f"Rate : {rate} ({rate_cnt})")
            print("Link : {}".format("https://www.coupang.com" + link))
            print("-"*100)
