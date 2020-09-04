# Python Web Scraping

# Title : Selenium
# Date : 2020-09-02
# Creator : tunealog

import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15", "Accept-Language": "ja-JP,ja"
}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class": "WHE7ib mpg5gc"})
print(len(movies))

with open("movie.html", "w", encoding="utf8") as f:
    f.write(soup.prettify())

for movie in movies:
    title = movie.find("div", attrs={"class": "WsMG1c nnK0zc"}).get_text()
    print(title)
