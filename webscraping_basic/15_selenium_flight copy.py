# Python Web Scraping

# Title : Selenium
# Date : 2020-08-31
# Creator : tunealog

from selenium import webdriver
browser = webdriver.Chrome()  # "./chromedriver.exe"
browser.maximize_window()

url = "https://flight.naver.com/flights/"

browser.get(url)

browser.find_element_by_link_text("가는날 선택").click()

# browser.find_elements_by_partial_link_text("27")[0].click()
# browser.find_elements_by_partial_link_text("28")[0].click()

# browser.find_elements_by_partial_link_text("27")[1].click()
# browser.find_elements_by_partial_link_text("28")[1].click()

browser.find_elements_by_partial_link_text("27")[0].click()
browser.find_elements_by_partial_link_text("28")[1].click()

browser.find_element_by_xpath(
    "//*[@id='recommendationList']/ul/li[1]").click()

browser.find_element_by_link_text("항공권 검색").click()

elem = browser.find_element_by_xpath(
    "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
print(elem.text)
