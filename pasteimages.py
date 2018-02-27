#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'paste images'

__author__ = 'yuyi-7'

import os
from  PIL import Image

class Paste(object):
	
	def __init__(self,path1,path2,path3):
		print('输入第一二个参数是第一二张图片路径，第三个参数是保存拼接图片的路径')
		self.path1 = path1
		self.path2 = path2
		self.path3 = path3

		
	def pastehigh(self):
		images=[]
		images.append(Image.open(self.path1))
		images.append(Image.open(self.path2))

		width,high = images[0].size
		width1,high1 = images[1].size
		traget = Image.new('RGB',(width,high+high1))
		traget.paste(images[0],(0,0))
		traget.paste(images[1],(0,high))
		traget.save(self.path3,quality = 100)
	
	def pastewidth(self):
		images = []
		images.append(Image.open(self.path1))
		images.append(Image.open(self.path2))
		width,high = images[0].size
		traget = Image.new('RGB',(width*2,high))
		traget.paste(images[0],(0,0))
		traget.paste(images[1],(width,0))
		traget.save(self.path3,quality = 100)
		
if __name__ == '__main__':
	desk = r'C:\Users\Administrator\Desktop'
	a=desk+'\\'+input('输入第一个图片名称：')
	b=desk+'\\'+input('输入第二张图片名称：')
	c=input('保存的名称：')
	c = desk+'\\'+c
	past = Paste(a, b, c)

	k = input('请输入是垂直(width)合成还是水平(high)合成：')
	if k == 'high':
		past.pastehigh()

	elif k == 'width':
		past.pastewidth()