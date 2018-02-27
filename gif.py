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

	def gethtml(self,http):
		html = self.down.get(http,3)
		soup = BeautifulSoup(html.text,'lxml')
		return soup

	def getgif(self):
	#	star_html = self.down.get('http://www.ddqsw.com/post',5)
		headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2372.400 QQBrowser/9.5.10548.400','Connection':'keep-alive','Cache-Control':'private, must-revalidate','Content-Encoding':'gzip','Content-Type':'text/html; charset=UTF-8'}
		star_html = requests.get('http://www.ddqsw.com/post',headers = headers)
		soup = BeautifulSoup(star_html.text,'lxml')
		try :
			li_lis = soup.find('div',class_='grid-gifs-wrap clearfix').find_all('a')
		except AttributeError :
			print('Error')
			self.gethtml('http://www.ddqsw.com/post')
			li_lis = soup.find('div',class_='grid-gifs-wrap clearfix').find_all('a')
		for i in li_lis:
			title = i.get_text()
			href = i.get('href')
<<<<<<< HEAD
		#	html = self.down.get(href,5)
			html = requests.get(href,headers=headers)
			html_soup = BeautifulSoup(html.text,'lxml')
			try:
				page = html_soup.find('div',class_='btn-group clearfix full-width pagination-block').find_all('a')[-1].get_text()
			except AttributeError:
				print('Error')
				self.gethtml(href)
				page = html_soup.find('div',class_='btn-group clearfix full-width pagination-block').find_all('a')[-1].get_text()
			for p in range(int(re.findall(r'\d+',page)[0])):
				page_url = href[0:-5]+'/'+str(p+1)+'.html'
			#	img_html = self.down.get(page_url,5)
				img_html = requests.get(page_url,headers=headers)
=======
			html = requests.get(href)
			html_soup = BeautifulSoup(html.text,'lxml')
			try:
				page = html_soup.find('div',class_='btn-group clearfix full-width pagination-block').find_all('a')[-1].get_text()
			except:
				page='0'
			for p in range(int(re.findall(r'\d+',page)[0])):
				page_url = href[0:-5]+'/'+str(p+1)+'.html'
				img_html = self.down.get(page_url,3)
			#	img_html = requests.get(page_url)
>>>>>>> 8f6b2212840cad3101aedff62e1b7067b27ac0ad
				img_soup = BeautifulSoup(img_html.text,'lxml')
				img_url = img_soup.find('div',class_='adetail')
				try:
					img = img_url.find_all('img')
				except AttributeError:
					print('Error')
					self.gethtml(page_url)
					img_url = img_soup.find('div',class_='adetail').find_all('img')
				if img_url==None:
					continue
				img = img_url.find_all('img')
				for m in img_url:
					myimg = m.get('src')
<<<<<<< HEAD
					dimg = self.down.get(myimg,5)
=======
					if myimg==None:
						continue
					dimg = self.down.get(myimg,3)
				#	dimg = requests.get(myimg)
>>>>>>> 8f6b2212840cad3101aedff62e1b7067b27ac0ad
					print('抓取%s，开始保存'%(myimg))
					f = open(self.path+'\\'+myimg[-9:],'ab')
					f.write(dimg.content)
					f.close()
#pa = input('保存路径：')
man = gif(r'D:\gif')
man.getgif()