# Python Web Scraping

# Title : Selenium
# Date : 2020-08-30
# Creator : tunealog

from selenium import webdriver
import time
browser = webdriver.Chrome()  # "./chromedriver.exe"

# 1. Access NAVER
browser.get("https://www.naver.com/")

# 2. Click Login Button
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. Input ID and PW
browser.find_element_by_id("id").send_keys("USER_ID")
browser.find_element_by_id("pw").send_keys("USER_PW")

# 4. Click Login Button
browser.find_element_by_id("log.login").click()
time.sleep(3)

# 5. Input new ID
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("MY_ID")

# 6. Output HTML
print(browser.page_source)

# 7. QUIT
browser.close()  # Current Tab
browser.quit()  # Browser
