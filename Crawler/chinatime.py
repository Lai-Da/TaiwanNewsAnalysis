import requests
from bs4 import BeautifulSoup as bs
import time

base_url = 'https://www.chinatimes.com'
url = 'https://www.chinatimes.com/realtimenews/260410/?page='
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

title_list = []
url_list = []
datetime_list = []
all_text_list = []

for page in range(1,11):
    r = requests.get(url+f'{page}', headers = headers)
    soup = bs(r.text,'html.parser')
    sel = soup('div', class_= 'articlebox-compact')
    time.sleep(2)
    for i in range(0,len(sel)):
        title_list.append(sel[i].select('h3')[0].text)
        url_list.append(base_url+sel[i].select('a')[0].get('href'))
   
for url in url_list:
    r = requests.get(url,headers=headers)
    soup = bs(r.text,'html.parser')
   
    datetime = soup.find('div',class_='meta-info')
    text = soup.find('div', class_='article-body').find_all('p')
    
    datetime_list.append(datetime.select('time')[0].text)
    text_list = []
    for i in range(0, len(text)):
        text_list.append(text[i].text)
    all_text_list.append(text_list)
    time.sleep(2)
    
index = ['time','title','url','text','src']
chinatime_data = []
for j in range(0,len(datetime_list[:5])):
    content = [datetime_list[j], title_list[j], url_list[j], all_text_list[j],'chinatime']
    chinatime_data.append(dict(zip(index, content)))
import json
chinatime_data_json = json.dumps(chinatime_data)

with open('chinatime_data_json.txt','w+') as f:
    f.write(chinatime_data_json)