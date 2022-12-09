from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup as bs
import time

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

opt = webdriver.ChromeOptions()
opt.add_argument('--user-agent=%s' % user_agent)

url = 'https://tw.stock.yahoo.com/tw-market/'
driver = webdriver.Chrome( options=opt)
driver.get(url)
time.sleep(2)

for i in range(1,11):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(0.5)
html = driver.page_source
driver.close()  # 關閉瀏覽器
soup = bs(html, 'html.parser')
st = soup('a', class_ = 'Fw(b) Fz(20px) Fz(16px)--mobile Lh(23px) Lh(1.38)--mobile C($c-primary-text)! C($c-active-text)!:h LineClamp(2,46px)!--mobile LineClamp(2,46px)!--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled')

title_list = []
url_list = []
datetime_list = []
text_list = []
for s in st:
    title_list.append(s.text)
    url_list.append(s.get('href'))


for url in url_list:
    r = requests.get(url,headers = headers)
    soup = bs(r.text,'html.parser')
    datetime = soup.select('div.caas-attr-time-style > time')
    text = soup.select('div.caas-body')
    
    datetime_list.append(datetime[0].text) 
    text_list.append(text[0].text)
    time.sleep(2)   

index = ['time','title','url','text','src']
yahoo_data = []
for j in range(0,len(datetime_list)):
    content = [datetime_list[j], title_list[j], url_list[j], text_list[j],'yahoo']
    yahoo_data.append(dict(zip(index, content)))

import json
yahoo_data_json = json.dumps(yahoo_data)
with open('yahoo_data_json.text') as f:
    f.write(yahoo_data_json)