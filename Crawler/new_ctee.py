import requests
from bs4 import BeautifulSoup as bs
import time
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
url = 'https://ctee.com.tw/tag/%E5%8F%B0%E8%82%A1/page/'

title_list = []
url_list = []
for i in range(22,25):
    r = requests.get(url+f'{i}', headers = headers)
    soup = bs(r.text,'html.parser')
    title = soup.find_all('h2', class_='title')
    for j in range(0,10):
        title_list.append(title[j].text[5:][:-3])
        url_list.append(title[j].select('a')[0].get('href'))
    time.sleep(2)

datetime_list = []
all_text_list = []
for url in url_list:
    r = requests.get(url,headers=headers)
    soup = bs(r.text,'html.parser')
    
    datetime = soup.find('time',class_='post-published updated')
    text = soup.find('div', class_='entry-content clearfix single-post-content').find_all('p')[:-5]
    datetime_list.append(datetime.text)
    text_list = []
    for j in range(0,len(text)):
        text_list.append(text[j].text.replace('\n','').replace('\t',''))
    all_text_list.append(text_list)
    time.sleep(2)

index = ['time','title','url','text','src']
ctee_data = []
for j in range(0,len(datetime_list)):
    content = [datetime_list[j], title_list[j], url_list[j], all_text_list[j], 'ctee']
    ctee_data.append(dict(zip(index, content)))

import pandas as pd

df_from_dict = pd.DataFrame(ctee_data, columns=['time', 'title', 'url', 'text', 'src'])
df_from_dict.to_csv('ctee_data1129-1201.csv', index=False)