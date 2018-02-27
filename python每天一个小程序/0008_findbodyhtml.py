#!/usr/bin/env python
# encoding: utf-8

'第 0008 题： 一个HTML文件，找出里面的正文。'

from urllib import request
from bs4 import BeautifulSoup

def inputad():
	ad = input('Please input the address: ')
	print(ad)
	return ad
	
def get_body(address):
	soup = BeautifulSoup(open(address,'r'),'html.parser')
	text = soup.body.get_text(strip = True)
	print(text)
	
if __name__ == '__main__':
	ad = inputad()
	get_body(ad)