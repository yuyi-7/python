#!/usr/bin/env python
# encoding: utf-8

'第 0006 题： 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。'

import os
import re
from mypython import dic

filetxt=[]
def getfile():
	path=input('please input path: ')
	for root,dirs,files in os.walk(path):
		for f in files:
			if f.lower().endswith('.txt'):
				filetxt.append(os.path.join(root,f))
				

def findword():
	word={}
	for i in range(len(filetxt)):
		with open(filetxt[i]) as f:
			words = f.read()
			word_dic = re.findall(r'[a-z]+',words.lower())
		
			for w in word_dic:
				if w not in word:
					word[w] = 1
				elif w in word:
					word[w] += 1
			s=dic.dict2list(word)
			sorte = sorted(s,key=lambda x:x[1],reverse = True)
			print('在%s文件中，单词%s出现了%s次\n'%(os.path.abspath(filetxt[i]),sorte[0][0],sorte[0][1]))
			
		
if __name__=='__main__':
	getfile()
	findword()