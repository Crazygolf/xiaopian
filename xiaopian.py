
import requests
from bs4 import BeautifulSoup
import re


url = 'https://www.xiaopian.com/html/gndy/dyzz/index.html'
url_requests = requests.get(url)
url_requests.encoding = 'GB2312'  # 修改编码
url_text = url_requests.text
bs = BeautifulSoup(url_text, 'html.parser')
a_ulink = bs.find_all('a', class_='ulink')
for a in a_ulink:
    print(a.text)
    print('http://www.xiaopian.com' + a['href'])

# 查找电影天堂中评分9.0以上的电影
