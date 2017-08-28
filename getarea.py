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
	wrok = xlwt.Workbook(encoding='utf-8',style_compression = 0)
	sheet = wrok.add_sheet('sheet1',cell_overwrite_ok=True)
	data = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\shangwu.xls')
	table = data.sheet_by_name('Sheet1')
	table2 = data.sheet_by_name('Sheet2')
	for i in range(table.nrows):
		nrow = table.row_values(i)

		if nrow[0] in shit:
		#	get_flag = True
			x.append(nrow[1])
			y.append(nrow[2])
			
			for j in range(table2.nrows):
				nrow2 = table2.row_values(j)

				if (x[flag1],y[flag1])==(nrow2[1],nrow2[2]):
					print(nrow2[0],nrow2[1],nrow2[2])
					sheet.write(flag,0,nrow2[0])
					sheet.write(flag,1,nrow2[1])
					sheet.write(flag,2,nrow2[2])
					real.append(nrow2[0])
			flag1 += 1
			flag += 1

	wrok.save(r'C:\Users\Administrator\Desktop\区域.xls')
	if flag<exit_flag1:
		print('输入错误，有数据不存在')
	return real

def creat():
	wrok = xlwt.Workbook(encoding='utf-8',style_compression=0)
	sheet = wrok.add_sheet('sheet2',cell_overwrite_ok=True)
	d = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\shangwu.xls')
	tabe = d.sheet_by_name('Sheet3')
	num = input('请确定是哪个区域：')
	d2 = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\区域%s.xls'%(num))
	table = d2.sheet_by_name('sheet1')
	data = []
	for k in range(table.nrows):
		nrowok = table.row_values(k)
		data.append(nrowok[0])

	data2 = []
	for j in range(len(data)):
		data2.append(data[j])

	for i in range(len(data)):

		flag1 = 0

		for flag1 in range(len(data2)):
			for m in range(tabe.nrows):
				nrow = tabe.row_values(m)

				if data[i] == data2[flag1]:
					sheet.write(i,flag1,0)
					
				elif (data[i],data2[flag1]) == (nrow[0],nrow[1]):
					sheet.write(i,flag1,nrow[2])
				
	for n in range(len(data)):
		sheet.write(len(data)+1,n,data[n])
	wrok.save(r'C:\Users\Administrator\Desktop\矩阵%s.xls'%num)

if __name__ =='__main__':
	caozuo = input('请确定要执行什么操作\n--------------------------------\n操作1：确定正确的地点坐标\n操作2：建立矩阵\n请输入1或者2：')
	if caozuo == '1':
		a = getin()
		getdata(a)
	elif caozuo == '2':
		creat()
	print('Wrok Done')