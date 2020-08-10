# Python Web Scraping

# Title : requests
# Date : 2020-08-10
# Creator : tunealog

import requests
res = requests.get("https://google.com")
res_err = requests.get("https://tunealog.tistory.com")

# Response Code : 200 - No Problem
print("Response Code : ", res.status_code)

# Response Code : 403 - Problem
print("Response Code : ", res_err.status_code)

if res_err.status_code == requests.codes.ok:
    print("No Problem")
else:
    print("Problem [Error Code ", res_err.status_code, "]")

# Start Web Scraping
res.raise_for_status()
print("Start Web Scraping")

# Error Log
# res_err.raise_for_status()
# print("Start Web Scraping")

# 14110
print(len(res.text))

with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)
