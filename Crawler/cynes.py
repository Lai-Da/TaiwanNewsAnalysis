import requests
from bs4 import BeautifulSoup as bs
import time

# 設定requests參數
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
url1 = 'https://api.cnyes.com/media/api/v1/newslist/category/headline?startAt=1669564800&endAt=1670515199&limit=30'
base_url = 'https://news.cnyes.com/news/id/'

# 準備容器
title_list1 = []
title_list2 = []
url_list1 = []
url_list2 = []
newsId_list = []
url_list = []
datetime_list = []
all_text_list = []

# 爬取第一頁的標題和網址
r1 = requests.get(url1, headers = headers)
for i in range(0,28):
    title_list1.append(r1.json()['items']['data'][i]['title'])
    newsId_list.append(r1.json()['items']['data'][i]['newsId'])

# 爬取第二頁開始的標題和網址
for n in range(2,11):
    url = 'https://api.cnyes.com/media/api/v1/newslist/category/headline?limit=30&startAt=1669564800&endAt=1670515199&page='+f'{n}'+'&startAt=1669564800&endAt=1670515199&limit=30'
    r2 = requests.get(url, headers = headers)
    time.sleep(2)
    for i in range(0,29):
        title_list2.append(r2.json()['items']['data'][i]['title'])
        newsId_list.append(r2.json()['items']['data'][i]['newsId'])


for newsId in newsId_list:
    url_list.append(base_url + str(newsId))
       
title_list = title_list1 + title_list2

# 爬取新聞的時間和內文
for url in url_list:
    r = requests.get(url, headers = headers)
    soup = bs(r.text, 'html.parser')
    datetime = soup.find('div', class_ = '_1R6L').find('time')
    text = soup.find('div', class_ = '_2E8y').find_all('p')
    datetime_list.append(datetime.text)
    
    text_list = []
    for i in range(0, len(text)):
        text_list.append(text[i].text)
    all_text_list.append(text_list)
    
    time.sleep(2)

# 將每一篇新聞合成一個dict
index = ['time','title','url','text','src']
cnyes_data = []
for j in range(0,len(datetime_list)):
    content = [datetime_list[j], title_list[j], url_list[j], all_text_list[j],'cnyes']
    cnyes_data.append(dict(zip(index, content)))

# dict to json and output
import json
cnyes_data_json = json.dumps(cnyes_data)
with open('cnyes_data_json.txt','w+') as f:
    f.write(cnyes_data_json)