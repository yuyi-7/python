#!/usr/bin/env python
# encoding: utf-8

import re

#在一个文件中查找特定的单词
n=0
word='you'

with open(r'C:\Users\Administrator\test.txt','r') as f:

	for lines in f.readlines():
		
		if re.findall(word,lines.lower()):
			n = n+1
print('有%d个%s'%(n,word))


with open(r'C:\Users\Administrator\test.txt','r') as f:
	n=0
	files = f.read()
	words = files.split()

	n = len(words)
	
print('有%d个单词'%n)
print(words)