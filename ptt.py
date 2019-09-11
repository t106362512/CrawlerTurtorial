import requests
from bs4 import BeautifulSoup
from datetime import timedelta
import json


#取得文章標題與連結
def get_links_from_index(page):
    soup = BeautifulSoup(page, features="lxml")
    divs = soup.find_all('div', class_='r-ent')
    linkList = list()
    for div in divs:
        soup_title = BeautifulSoup(str(div), features="lxml")
        title = soup_title.find_all('div', class_='title')
        news_title = title[0].text.strip()
        try:
            link = title[0].find('a')['href'].strip()
        except:
            continue
        if '[公告]' in news_title or '[協尋]' in news_title:
            continue
        linkList.append([news_title, link])

    # 因為每一個 index.html中的文章，最新的那篇是在最底下，所以做個 reversed
    # 這樣最新的文章就會是在 linkList[0]
    linkList = list(reversed(linkList))
    return linkList


#從首頁進入並設定cookie


ptt = "https://www.ptt.cc"
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
s = requests.Session()
s.post(ptt + "/ask/over18", data={'yes': 'yes'})
page = s.get(url).text


if __name__ == '__main__': 
    #秀出連結
    line= get_links_from_index(page)
    for item in line:
        print(item)
