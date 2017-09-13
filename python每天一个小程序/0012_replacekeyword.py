#!/usr/bin/env python
# encoding: utf-8

'敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。'

import re

def judge(word):
	strs = '**'
	flag = False
	with open('filter_words.txt','r') as f:
		for line in f:
		#	line = line.split(' ')
			line = line.strip()
		#	line = re.split(' ',line)
			lon = len(re.split(r'%s' %(line), word))
			if lon > 1:
				finds = line
				flag = True
		
		if flag == True:
			
			b = re.split(r'%s' % (finds.strip()), word)
			print(strs.join(b))
		
		else:
			print(word)

if __name__ == "__main__":
	while True:
		
		word = input('Please input the words: ')
		judge(word)
