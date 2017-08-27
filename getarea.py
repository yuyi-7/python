#!/usr/bin/env python
# encoding: utf-8

import xlrd
import xlwt

def getin():
	a = []
	while True:
		a = input('请输入客户订单号,并以#结束:')
		if a == '#':
			break
		a = str(a)
	return a

def getdata(shit):
	flag1 = 0
	flag2 = 0
	flag3 = 0
	x = []
	y = []
	real = []
	data = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\shangwu.xls')
	table = data.sheet_by_name('Sheet1')
	table2 = data.sheet_by_name('Sheet2')
	for i in table.nrows:
		nrow = table.row_valuse[i]

		if nrow[0] == shit:
			x[flag1],y[flag2] = nrow[1],nrow[2]

			for j in table2.nrows:
				nrow2 = table2.row_valuse[j]

				if (x[flag1],y[flag2])==(nrow2[1],nrow2[2]):
					real[flag3] = nrow[0]
					flag3 += 1

			flag1 += 1
			flag2 += 1

	return real

def writexle(realdata):
	flag = 0
	wrok = xlwt.Workbook(encoding='utf-8',style_compression = 0)
	sheet = wrok.add_sheet('sheet1',cell_overwrite_ok=True)
	data = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\shuangwu.xls')
	table = data.sheet_by_name('Sheet2')

	for i in table.nrows:
		nrow = table.row_valuse[i]
		if realdata[flag] == norw[0]:
			x,y = nrow[1],nrow[2]
			sheet.write(flag,0,realdata[flag])
			sheet.write(flag,1,x)
			sheet,write(flag,2,y)

	wrok.save(r'C:\Users\Administrator\Desktop\区域.xls')

if __name__ =='__main__':
	a = getin()
	b = []
	b = getdata(a)
	writexle(b)
	print('Wrok Done')