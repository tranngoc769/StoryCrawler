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
# getListChapter("https://truyenfull.vn/toi-thay-hoa-vang-tren-co-xanh/")

def getChapter(text):
    pos = text.find(':')
    if (pos== -1): pos = len(text)
    chap = text[0:pos]
    return [int(s) for s in chap.split() if s.isdigit()][0]
def getListChapter(url):
    global wd
    wd.get(url)
    soup = BeautifulSoup(wd.page_source, features="lxml")
    isPanigation = soup.find_all('ul', {'class','pagination pagination-sm'})
    if len(isPanigation) != 0:
        lastAPageElement = isPanigation[len(isPanigation)- 1].find_all('a')[0]
        newUrl = lastAPageElement.attrs['href']
        wd.get(newUrl)
        soup = BeautifulSoup(wd.page_source, features="lxml")
    ColumsChapters = soup.find_all('ul', {'class','list-chapter' })
    listEndChapters = ColumsChapters[len(ColumsChapters)-1].contents
    lastChapter = listEndChapters[len(listEndChapters) - 1]
    a_element = lastChapter.find_all('a')[0]
    totalChapter = getChapter(a_element.text)
    return totalChapter
