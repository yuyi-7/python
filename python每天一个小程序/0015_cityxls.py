#!/usr/bin/env python
# encoding: utf-8
'''
第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：
{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
'''

import xlrd
import xlwt
import re
work = xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet = work.add_sheet('Sheet1',cell_overwrite_ok=True)
inf = re.compile(r'\"(\d)\" : \"(\w+)\"')
conut = 0
with open('city.txt','r') as f:
	line = f.read()
	for data in inf.findall(line):
		for i in range(len(data)):
			sheet.write(conut,i,data[i])
		conut += 1
work.save('city.xls')