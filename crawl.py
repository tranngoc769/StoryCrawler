from selenium import webdriver
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import re
options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")
options.add_argument('-headless')
options.add_argument('-no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--log-level=3')
options.add_argument('-disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver.exe',options=options)


def getListUrl(path = "url.txt"):
    listString = []
    with open(path, encoding="UTF-8", mode="r") as f:
        listString = f.readlines()
        listString = [x.strip() for x in listString]
    return listString