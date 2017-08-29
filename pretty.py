#!/usr/bin/env python
# encoding: utf-8

from bs4 import BeautifulSoup
import os,random,time
import urllib.request

def mkfile():
	path = r'C:\Users\Administrator\Desktop\wed'
	new_path = os.path.join(path,'wed_picture')
	if not os.path.isdir(new_path):
		os.mkdir(new_path)
	return new_path

def wedloop(new_path):
#	page = input('要抓取多少页照片:')
#	page = int(page)
	count = 0
	name = range(100)
	for i in range(10):
		wed = urllib.request.urlopen(r'http://www.ddqsw.com/post-xNpbamz9/%d.html'%(i+1))
		soup = BeautifulSoup(wed,'lxml')
		myimg = soup.find_all('img',alt='打个喷嚏把旁边两位美女的裙子都吹开了，我也想拥有这样的能力')
		for j in myimg:
			if(j.get('class')==['gif-box-img']):
				continue
			link = j.get('src')
			pic_name = os.path.join(new_path,time.strftime('%H-%M-%S')+random.choice('qwertyuiopasdfghjklzxcvbnm')+'.gif')
			print(link)
			urllib.request.urlretrieve(link,pic_name)

if __name__ == '__main__':
	wedloop(mkfile())