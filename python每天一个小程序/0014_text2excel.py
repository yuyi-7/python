#!/usr/bin/env python
# encoding: utf-8
'''
纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
{
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}
请将上述内容写到 student.xls 文件中
'''
import xlwt
import re

book = xlwt.Workbook(encoding = 'utf-8')
sheet = book.add_sheet('student',cell_overwrite_ok = True)
line = 0
infon = re.compile(r'\"(\d+)\":\[\"(\w+)\",(\d+),(\d+),(\d+)\]')
with open('student.txt','r') as f:
	data = f.read()
	for x in infon.findall(data):
		for i in range(len(x)):
			sheet.write(line,i,x[i])
		line += 1

book.save('student.xls')