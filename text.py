#!/usr/bin/env python
# encoding: utf-8

'第 0010 题： 使用 Python 生成类似于下图中的字母验证码图片'

from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

w=60*4
h=60

image = Image.new('RGB',(w,h))

font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)

draw = ImageDraw.Draw(image)

for x in range(w):
	for y in range(h):
		draw.point((x,y),fill = (random.randint(64,225),random.randint(64,225),random.randint(64,225)))

for i in range(4):
	draw.text((i*60+10,10),chr(random.randint(65,90)),font = font,fill = (random.randint(32,125),random.randint(32,125),random.randint(32,125)))

image = image.filter(ImageFilter.BLUR)

image.show()
					