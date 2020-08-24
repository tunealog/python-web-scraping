# Python Web Scraping

# Title : BeautifulSoup4
# Date : 2020-08-24
# Creator : tunealog

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15"}
url = "https://search.daum.net/search?w=tot&q=2019년영화순위&DA=MOR&rtmaxcoll=MOR"
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

images = soup.find_all("img", attrs={"class": "thumb_img"})
for image in images:
    image_url = image["src"]
    if image_url.startswith("//"):
        image_url = "https:" + image_url
    print(image_url)
