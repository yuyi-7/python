#!/usr/bin/env python
# encoding: utf-8

'第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。'

import os
import re

def jage():
	with open('filter_words.txt','r') as f:
		words = [files.split() for files in f.read()]
	
		while True:
			a = input('Please input words: ')
			for w in words:
				if w in a:
					a = a.replace(w, '*'*len(x))
			print(a)
			
if __name__ == '__main__':
	jage()