# Python Web Scraping

# Title : Web Scraping Project
# Date : 2020-09-10
# Creator : tunealog

import re
import requests
from bs4 import BeautifulSoup


def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


def print_news(index, title, link):
    print("{}. {}".format(index+1, title))
    print("  (링크 : {})".format(link))


def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)

    # 흐림, 어제보다 OO°C 높아요
    cast = soup.find("p", attrs={"class": "cast_txt"}).get_text()
    # 현재 OO°C (최저 OO°C / 최고 OO°C)
    curr_temp = soup.find(
        "p", attrs={"class": "info_temperature"}).get_text().replace("도씨", "")
    min_temp = soup.find("span", attrs={"class": "min"}).get_text()
    max_temp = soup.find("span", attrs={"class": "max"}).get_text()
    # 오전 강수확률 OO% / 오후 강수확률 OO%
    morning_rain_rate = soup.find(
        "span", attrs={"class": "point_time morning"}).get_text().strip()
    afternoon_rain_rate = soup.find(
        "span", attrs={"class": "point_time afternoon"}).get_text().strip()

    # 미세먼지 OO㎍/㎥ 좋음
    # 초미세먼지 OO㎍/㎥ 좋음
    dust = soup.find("dl", attrs={"class": "indicator"})
    pm10 = dust.find_all("dd")[0].get_text()
    pm25 = dust.find_all("dd")[1].get_text()

    print(cast)
    print("현재 {} (최저 {} / 최고 {})".format(curr_temp, min_temp, max_temp))
    print("오전 {} / 오후 {}".format(morning_rain_rate, afternoon_rain_rate))
    print()
    print("미세먼지 {}".format(pm10))
    print("초미세먼지 {}".format(pm25))
    print()


def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)
    news_list = soup.find(
        "ul", attrs={"class": "hdline_article_list"}).find_all("li", limit=3)
    for index, news in enumerate(news_list):
        title = news.div.a.get_text().strip()
        link = url + news.find("a")["href"]
        print_news(index, title, link)
    print()


def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find(
        "ul", attrs={"class": "type06_headline"}).find_all("li", limit=3)
    for index, news in enumerate(news_list):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1
        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        print_news(index, title, link)
    print()


def scrape_english():
    print("[오늘의 영어회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english#;"
    soup = create_soup(url)
    sentences = soup.find_all("div", attrs={"id": re.compile("^conv_kor_t")})
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]:
        print(sentence.get_text().strip())
    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())
    print()


if __name__ == "__main__":
    # scrape_weather()
    # scrape_headline_news()
    # scrape_it_news()
    scrape_english()
