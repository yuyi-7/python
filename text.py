#!/usr/bin/env python
# encoding: utf-8

'第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。'

import os
import re

tool=[]
def getfiles():
	path=input('please input the path: ')
	for root,dirs,files in os.walk(path):
		for f in files:
			if f.lower().endswith('.py'):
				
				tool.append(root+'/'+f)
			
def cul():
	n=r=z=0
	for i in range(len(tool)):
		with open(tool[i],'r',encoding='utf-8') as f:
			for lines in f.readline():
				n = n + 1
				
				
				if lines.strip() == '':
						r = r + 1
				
				if re.match(r'^#',lines.strip()):
					z += 1
			
					
	print('你总共写了%d行代码，%d个空行，%d行注释'%(n,r,z))
	
if __name__=='__main__':
	getfiles()
	cul()
					