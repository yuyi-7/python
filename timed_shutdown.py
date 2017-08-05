import os,time,re
print('-----------------------------------------------------')
print('这是一个 定时关机 脚本\n\n如果想取消定时关机请输入 off \n\n')
print('说明：此脚本有两种模式\n\n  模式1为设定关机时间点,比如设定23:50关机，脚本便收集系统时间，设定在23:50关机\n\n  模式2为设定时间段,比如设定12:00便在12小时后关机，或是设定50便在50分钟后关机')
print('-----------------------------------------------------')
mode=input('请输入 mode1 或者是 mode2 或是取消关机计划:')

if mode=='mode1':
 while True:
 	input_time=input('请输入关机时间，格式为 小时:分钟 ：')
 	
 	if re.match(r'^\d{2}\:\d{2}$',input_time):
 	 hourset = int(input_time[0:2])
 	 minset = int(input_time[3:5])
 	 break
 	
 	else: print('输入不正确，请重新输入\n')

 print('关机时间设定为%d:%d'%(hourset,minset))

 mytime=time.strftime('%H:%M:%S')
 myhour =	int(mytime[0:2])
 mymin	=	int(mytime[3:5])

 print('系统时间为%d:%d'%(myhour,mymin))

 if hourset>24:
	  hourset=24
	  minset=0
 if minset>60:
	   minset=60
 if hourset<myhour:
	  hourset=hourset+24

 sec=(hourset+(minset/60.0)-myhour-(mymin/60.0))*3600
 print('距离关机还有 %d 秒' %sec)
 os.system('shutdown -s -t %d' %sec )

elif mode=='mode2':
	print('请输入要在多久后关机')
	while True:
	 input_times=input('格式为 小时:分钟 如01:30 或者 直接输入分钟数 ：')
	
	 if re.match(r'^\d{2}\:\d{2}$',input_times):
	 	hoursset= int(input_times[0:2])
	 	minsset= int(input_times[3:5])
	 	sec=hoursset*3600+minsset*60
	 	break
		
	 elif re.match(r'[\d]+',input_times):
		 sec = int(input_times) *60
		 break
	 else:print('格式不正确，请重新输入')
	os.system('shutdown -s -t %d' %sec )

elif mode=='off':
	os.system('shutdown -a')
	
