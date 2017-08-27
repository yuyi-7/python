#!/usr/bin/env python
# encoding: utf-8

import xlrd
import xlwt
import random

def getin():
	b = []
	print('请输入客户订单，并以#结束输入：')
	while True:
		a = input()
		if a == '#':
			break
		a = str(a)
		b.append(a)
	return b

def getdata(shit):
	exit_flag1 = len(shit)
	get_flag = False
	flag = 0
	flag1 = 0
	x = []
	y = []
	real = []
	data = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\shangwu.xls')
	table = data.sheet_by_name('Sheet1')
	table2 = data.sheet_by_name('Sheet2')
	for i in range(table.nrows):
		nrow = table.row_values(i)

		if nrow[0] in shit:
		#	get_flag = True
			x.append(nrow[1])
			y.append(nrow[2])
			flag += 1
			for j in range(table2.nrows):
				nrow2 = table2.row_values(j)

				if (x[flag1],y[flag1])==(nrow2[1],nrow2[2]):
					print(nrow2[0])
					real.append(nrow2[0])
			flag1 += 1

	if flag<exit_flag1:
		print('输入错误，有数据不存在')

	return real

def writexle(realdata):
	exit_flag = len(realdata)
	flag = 0
	wrok = xlwt.Workbook(encoding='utf-8',style_compression = 0)
	sheet = wrok.add_sheet('sheet1',cell_overwrite_ok=True)
	data = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\shangwu.xls')
	table = data.sheet_by_name('Sheet2')
	for i in range(table.nrows):
		nrow = table.row_values(i)
		if realdata[flag] == nrow[0]:
			x,y = nrow[1],nrow[2]
			sheet.write(flag,0,realdata[flag])
			sheet.write(flag,1,x)
			sheet.write(flag,2,y)
			flag += 1
		if flag == exit_flag:
				break

	wrok.save(r'C:\Users\Administrator\Desktop\区域.xls')

if __name__ =='__main__':
	a = getin()
	b = []
	b = getdata(a)
	writexle(b)
	print('Wrok Done')