# Python Web Scraping

# Title : Selenium
# Date : 2020-08-28
# Creator : tunealog

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()  # "./chromedriver.exe"
browser.get("https://www.naver.com/")
elem = browser.find_element_by_class_name("link_login")
elem.click()
browser.back()
browser.forward()
browser.refresh()
browser.back()
elem = browser.find_element_by_id("query")
elem.send_keys("tunealog")
elem.send_keys(Keys.ENTER)
