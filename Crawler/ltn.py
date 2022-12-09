import requests
from bs4 import BeautifulSoup 
import time

headers = {"cookie":"softPush = 1",
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
r1 = requests.get("https://news.ltn.com.tw/ajax/breakingnews/business/1",headers = headers)

title_list1 = []
title_list2 = []
url_list1 = []
url_list2 = []
datetime_list = []
text_list = []

for i in range(0,20):
    page1 = r1.json()['data']
    title_list1.append(page1[i]['title'])
    url_list1.append(page1[i]['url'])
        
for n in range(2,3):
    url = f"https://news.ltn.com.tw/ajax/breakingnews/business/{n}"
    r = requests.get(url,headers = headers)
    page = r.json()['data']
    time.sleep(2)
    for i in range(((n-1)*20),(((n-1)*20)+19)):
        data_dict = page[f'{i}']
        title_list2.append(data_dict['title'])
        url_list2.append(data_dict['url'])
title_list = title_list1 + title_list2    
url_list = url_list1 + url_list2

for url in url_list:
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.text,'html.parser')
    datetime = soup.find('span',class_='time')
    text = soup.find('div',class_ = 'text').find_all('p')
    datetime_list.append(datetime.text)
    for n in text:
        text_list.append(n.text.replace('請繼續往下閱讀...','').replace('一手掌握經濟脈動','').replace('點我訂閱自由財經Youtube頻道','').replace('不用抽 不用搶 現在用APP看新聞 保證天天中獎','').replace('點我下載APP','').replace('按我看活動辦法',''))
index = ['time','title','url','text','src']
ltn_data = []
for j in range(0,len(datetime_list)):
    content = [datetime_list[j], title_list[j], url_list[j], text_list[j],'ltn']
    ltn_data.append(dict(zip(index, content)))

import json
ltn_data_json = json.dumps(ltn_data)
with open('ltn_data_json.text','w') as f:
    f.write(ltn_data_json)