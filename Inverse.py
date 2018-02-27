#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
import os
import sys


class Images(object):
	def __init__(self,name):
		self.path = os.getcwd()
		self.name = name
		self.pl = Image.open(os.path.join(self.path,'%s'%(name)))
		#print(os.path.join(self.path,'%s'%(self.name)))
		
	def change(self):
		self.pm = self.pl.point(lambda i:255-i)
		
	def show(self):
		self.pm.show()
	
	def save(self):
		new_path = os.path.join(self.path,'反相')
		if not os.path.isdir(new_path):			
			os.mkdir(new_path)
		#print(new_path)
		save_path = os.path.join(new_path,'c_%s'%(self.name))
		#print(save_path)
		self.pm.save(save_path)
		
if __name__ == '__main__':
	print('-------------------------\n说明：请把本程序放在图片同目录下\n-------------------------')
	name = []
	path = os.getcwd()
	find = os.listdir(path)
	print('正在扫描当前目录的图片')
	for i in find:
		if i[-3:] == 'png':
			name.append(i)
		elif i[-3:] == 'jpg':
			name.append(i)
	if name == []:
		print('未找到图片，终止程序')
		syss = input('请输入q退出程序')
		if syss == 'q':
			sys.exit()
	else :
		print('已找到图片')
		print(name)

	count = 0
	for j in name:
		#print(j)
		image = Images(str(j))
		image.change()
		image.save()
		print('正在处理第%d张'%(count+1))
		count = count + 1

	print('处理完成,图片已保存在本目录的反相文件夹下')
	input()