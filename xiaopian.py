# 查找电影天堂中评分9.0以上的电影

import requests
from bs4 import BeautifulSoup
import re

# url = 'https://www.xiaopian.com/html/gndy/dyzz/index.html'
url = 'https://www.xiaopian.com/html/gndy/jddyy/'

# def get_film(url):  # get 9+ film and the url
# 	url_requests = requests.get(url)
# 	url_requests.encoding = 'GB2312'  # 修改编码
# 	url_text = url_requests.text
# 	bs = BeautifulSoup(url_text, 'html.parser')
# 	a_ulink = bs.find_all('a', class_='ulink')
# 	for a in a_ulink:
# 	    # text = re.findall('-?\d+\.\d*e?-?\d*?分', a.text)
# 	    # text = re.findall('-?([1-9]\d*\.\d*|0\.\d*[1-9]\d*|0?\.0+|0)$分', a.text)
# 	    # text_all = re.findall((r"\d+\.?\d*", a.text))
# 	    if text:  # tell text is not empty
# 	    	new_text = re.sub("\D","",text[0])
# 	    	if int(new_text) >= 90 and int(new_text) < 100:  # convert text to number
# 		    	print(a.text)
# 		    	print('http://www.xiaopian.com' + a['href'])


def get_film(url):  # get 9+ film and the url
	url_requests = requests.get(url)
	url_requests.encoding = 'GB2312'  # 修改编码
	url_text = url_requests.text
	bs = BeautifulSoup(url_text, 'html.parser')
	a_ulink = bs.find_all('a', class_='ulink')
	for a in a_ulink:
	    text_all = re.findall(r"\d+\.?\d*分", a.text)  # find 9+ score title
	    if text_all:  # tell text is not empty
	    	i = 0
	    	for text in text_all:
	    		if float(text.replace('分', '')) >= 9.0 and float(text.replace('分', '')) <= 10.0:  # replace '分' with '', convert text to number
	    			i += 1
	    	if i >= 1:
	    		print(a.text)  # print title of film
	    		print('http://www.xiaopian.com' + a['href'])  # print url of film


def get_page_number(url):
	page_number = 0
	url_requests = requests.get(url)
	bs = BeautifulSoup(url_requests.text, 'html.parser')
	select_all = bs.find_all('select', {'name':'select'})
	for select in select_all:
		option_all = select.find_all('option')
	return len(option_all)


def get_all_films(url):
	for i in range(1, get_page_number(url)+1):
		if i == 1:
			get_film(url)
		else:
			get_film("https://www.xiaopian.com/html/gndy/jddyy/index_%d.html" % i)

get_all_films(url)


