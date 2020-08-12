# Python Web Scraping

# Title : User Agent
# Date : 2020-08-12
# Creator : tunealog

import requests
url = "https://tunealog.tistory.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
res = requests.get(url, headers=headers)

# Start Web Scraping
res.raise_for_status()

with open("tunealog.html", "w", encoding="utf-8") as f:
    f.write(res.text)
