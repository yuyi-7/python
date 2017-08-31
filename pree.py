#!/usr/bin/env python
# encoding: utf-8

import requests
from bs4 import BeautifulSoup
import os
import random
from mypython import Download

path = r'D:\mzitu'
if not os.path.isdir(path):
	os.mkdir(path)

download = Download.download(referer="http://www.mzitu.com/101553")

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
'Referer':"http://www.mzitu.com/101553"}
star_html = download.get('http://www.mzitu.com/all',3)
soup = BeautifulSoup(star_html.text,'lxml')
li_list = soup.find('div',class_='all').find_all('a')
for li in li_list:
	title = li.get_text()
	new_path = os.path.join(path,title)
	if not os.path.isdir(new_path):
		os.mkdir(new_path)
	href = li.get('href')
	html = download.get(href,3)
	html_soup = BeautifulSoup(html.text,'lxml')
	max_span = html_soup.find('div',class_='pagenavi').find_all('span')[-2].get_text()
	for page in range(int(max_span)):
		page_url = href+'/'+str(page)
		img_html = download.get(page_url,3)
		img_soup = BeautifulSoup(img_html.text,'lxml')
		img_url = img_soup.find('div',class_='main-image').find('img').get('src')
		img = download.get(img_url,3)
		print('抓取%s,开始保存'%(img_url))
		f = open(new_path+'\\'+random.choice('rtyugdsczxbgd263561')+img_url[-7:],'ab')
		f.write(img.content)
		f.close()