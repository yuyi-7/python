#!/usr/bin/env python
# encoding: utf-8

'第 0009 题： 一个HTML文件，找出里面的链接。'

from urllib import request
from bs4 import BeautifulSoup

def gethtml():
	ad = input('Please input html address:')
	return ad
	
def findlink(address):
	soup = BeautifulSoup(open(address,'r'),'html.parser')
	for i in soup.find_all('a'):
		print(i.get('href'))
		
if __name__ == '__main__':
	a = gethtml()
	findlink(a)