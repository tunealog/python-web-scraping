# Python Web Scraping

# Title : Selenium
# Date : 2020-09-05
# Creator : tunealog

from bs4 import BeautifulSoup
import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

# Move Page
# url = "https://play.google.com/store/movies/top"
url = "https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA"
browser.get(url)

# Down Scroll
# browser.execute_script("window.scrollTo(0,1080)")


interval = 2

prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break

    prev_height = curr_height

print("Scroll End")


soup = BeautifulSoup(browser.page_source, "lxml")

# movies = soup.find_all("div", attrs={"class": ["ImZGtf mpg5gc", "Vpfmgd"]})
movies = soup.find_all("div", attrs={"class": "Vpfmgd"})
print(len(movies))


for movie in movies:
    title = movie.find("div", attrs={"class": "WsMG1c nnK0zc"}).get_text()

    original_price = movie.find("span", attrs={"class": "SUZt4c djCuy"})
    # if original_price:
    #     original_price = original_price.get_text()
    # else:
    #     continue

    price = movie.find(
        "span", attrs={"class": "VfPpfd ZdBevf i5DZme"}).get_text()

    link = movie.find("a", attrs={"class": "JC71ub"})["href"]
    print(f"Title : {title}")
    print(f"Original Price : {original_price}")
    print(f"Price : {price}")
    print("Link : ", "https://play.google.com" + link)
    print("-" * 100)
browser.quit()
