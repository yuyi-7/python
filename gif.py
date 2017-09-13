#!/usr/bin/env python
# encoding: utf-8
import requests
import os,random
from bs4 import BeautifulSoup
from mypython import Download
import re

class gif(object):
	def __init__(self,path):
		self.path = path
		if not os.path.isdir(path):
			os.mkdir(path)
		self.down = Download.download()

	def getgif(self):
		star_html = self.down.get('http://www.ddqsw.com/post',3)
		soup = BeautifulSoup(star_html.text,'lxml')
		li_lis = soup.find('div',class_='grid-gifs-wrap clearfix').find_all('a')
		for i in li_lis:
			title = i.get_text()
			href = i.get('href')
			html = self.down.get(href,3)
			html_soup = BeautifulSoup(html.text,'lxml')
			page = html_soup.find('div',class_='btn-group clearfix full-width pagination-block').find_all('a')[-1].get_text()
			for p in range(int(re.findall(r'\d+',page)[0])):
				page_url = href[0:-5]+'/'+str(p+1)+'.html'
				img_html = self.down.get(page_url,3)
				img_soup = BeautifulSoup(img_html.text,'lxml')
				img_url = img_soup.find('div',class_='adetail')
				img = img_url.find_all('img')
				for m in img_url:
					myimg = m.get('src')
					dimg = self.down.get(myimg,3)
					print('抓取%s，开始保存'%(myimg))
					f = open(self.path+'\\'+myimg[-9:],'ab')
					f.write(dimg.content)
					f.close()
#pa = input('保存路径：')
man = gif(r'D:\gif')
man.getgif()