#!/usr/bin/env python
# encoding: utf-8

from bs4 import BeautifulSoup
import os,random,sys,time
import urllib.request

class Wedpicture(object):
	def __init__(self,url):
		self.url = url

	def mkdirfide(self):
		path = input('Please input the path:')
		new_path = os.path.join(path,u'wed_picture')
		if not os.path.isdir(new_path):
			os.mkdir(new_path)
		self.new_path = new_path

	def page_loop(self):
		cont = urllib.request.urlopen(self.url)
		soup = BeautifulSoup(cont,'lxml')
		myimg = soup.find_all('img',class_='BDE_Image')
		for i in myimg:
			link = i.get('src')
			pic_num = os.path.join(self.new_path,time.strftime('%H-%M-%S')+random.choice('qwertyuiopasdfghjklzxcvbnm')+'.jpg')
			print(link)
			urllib.request.urlretrieve(link,pic_num)

if __name__ =='__main__':
	pa = Wedpicture('http://tieba.baidu.com/p/2166231880')
	pa.mkdirfide()
	pa.page_loop()