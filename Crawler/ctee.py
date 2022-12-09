import requests
from bs4 import BeautifulSoup as bs
import time


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
url = 'https://ctee.com.tw/livenews/aj/page/'
title_list = []
url_list = []
datetime_list = []
text_list = []
    
for i in range(1,3):
    r = requests.get(url+f'{i}', headers = headers)
    soup = bs(r.text,'html.parser')
    title = soup.find_all('div', class_='item-content')
    time.sleep(2)

    for x in range(0,len(title)):
        title_list.append(title[x].select('a')[1].text[:-16][13:])
        url_list.append(title[x].select('a')[1].get('href'))

for url in url_list:
    r = requests.get(url,headers=headers)
    soup = bs(r.text,'html.parser')
    
    datetime = soup.find('div',class_='post-meta-date')
    text = soup.find('div', class_='entry-content clearfix single-post-content')
    
    datetime_list.append(datetime.text)
    text_list.append(text.text)
    time.sleep(2)

index = ['time','title','url','text','src']
ctee_data = []
for j in range(0,len(datetime_list)):
    content = [datetime_list[j], title_list[j], url_list[j], text_list[j], 'ctee']
    ctee_data.append(dict(zip(index, content)))

import json
ctee_data_json = json.dumps(ctee_data)

with open('ctee_data_json.txt','w+') as f:
    f.write(ctee_data_json)