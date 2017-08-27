#!/usr/bin/env python
# encoding: utf-8

from bs4 import BeautifulSoup
import os,random,sys,time
import urllib.request

def mkdirfide():
	path = input('Please input the path:')
	new_path = os.path.join(path,u'wed_picture')
	if not os.path.isdir(new_path):
		os.mkdir(new_path)
	return new_path

def page_loop(new_path):
	
	cont = urllib.request.urlopen(r'http://tieba.baidu.com/p/2166231880')
	soup = BeautifulSoup(cont,'lxml')
	myimg = soup.find_all('img',class_='BDE_Image')
	count = 0
	nam = range(100)
	for i in myimg:
		link = i.get('src')
		pic_num = os.path.join(new_path,str(nam[count])+'.jpg')
		count += 1
		print(link)
		urllib.request.urlretrieve(link,pic_num)

if __name__ =='__main__':
	page_loop(mkdirfide())