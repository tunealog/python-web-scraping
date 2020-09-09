# Python Web Scraping

# Title : Quiz
# Date : 2020-09-08
# Creator : tunealog

# ######### Sample #########
# =========== 매물 1 ===========
# 거래 :   월세
# 면적 :   109/84  (공급/전용)
# 가격 :   30,000/240  (만원)
# 동　 :   206동
# 층　 :   고/28
# =========== 매물 2 ===========
#    ...
# ##########################

import requests
from bs4 import BeautifulSoup
i = 0
max_no = 5
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15"}
url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

sell_type = soup.find_all(
    "td", attrs={"class": "col1"})
sell_size = soup.find_all(
    "td", attrs={"class": "col2"})
sell_price = soup.find_all(
    "td", attrs={"class": "col3"})
sell_place = soup.find_all(
    "td", attrs={"class": "col4"})
sell_floor = soup.find_all(
    "td", attrs={"class": "col5"})
for i in range(max_no):

    print(f"========== 매물 {i+1} ==========")
    print(f"거래 :  {sell_type[i].get_text()}")
    print(f"면적 :  {sell_size[i].get_text()} (공급/전용)")
    print(f"가격 :  {sell_price[i].get_text()} (만원)")
    print(f"동　 :  {sell_place[i].get_text()}")
    print(f"층　 :  {sell_floor[i].get_text()}")
    i += 1
