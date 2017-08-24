#!/usr/bin/env python
# encoding: utf-8

'第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。'

def judg():
	with open('filter_words.txt','r') as f:
		files = f.read()
		words = files.split()
		
		while True:
			a = input('Please input words:')
			if a in words:
				print('Freedom')
			else:
				print('Human Rights')
				
if __name__ == '__main__':
	judg()