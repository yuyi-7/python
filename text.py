#!/usr/bin/env python
# encoding: utf-8

'第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。'

import os
from PIL import Image
iw = 1136
ih = 640

def main():
	path = input('please input the path of images: ')


	for root, dirs, files in os.walk(path):
		for f in files :
			if f.lower().endswith('jpg'):
				images=Image.open(path+'/'+f)
				target = chagesize(images)
				target.save(path+'/'+'iphone5_'+f)
        
        
def chagesize(images):
	
	w,h = images.size
	if w>iw:
	   	h=iw * h//w
	   	w=iw
	elif h>640:
		  w = ih * w//h
		  h=ih
	target = images.resize((w,h),Image.ANTIALIAS)
	return target
	
if __name__=='__main__':
	main()