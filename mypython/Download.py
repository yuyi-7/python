#!/usr/bin/env python
# encoding: utf-8

import os,re,random,requests
import time
from bs4 import BeautifulSoup

class download(object):
	def __init__(self,referer=''):
		self.referer = referer
		self.iplis = []
		headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0','Referer':referer}
		ht = requests.get('http://www.xicidaili.com',headers = headers)
		soup = BeautifulSoup(ht.text,'lxml')
		for i in soup.find_all('tr',class_='odd'):
			j=i.find_all('td')[1].get_text()
			self.iplis.append(j.strip())
		self.uesr_agent_lis=["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]

	def get(self,url,timeout,proxy=None,num_retries=6):
		ua = random.choice(self.uesr_agent_lis)
		headers = {'User-Agent':"ua",'Referer':self.referer}
		if proxy == None:
			try:
				respones = requests.get(url,headers = headers,timeout=timeout)
				return respones
			except:
				if num_retries > 0:
					time.sleep(5)
					print(u'获取网页出错，5秒后讲获取第',(7-num_retries),u'次')
					return self.get(url,timeout,num_retries-1)
				else:
					print(u'开始使用代理')
					time.sleep(5)
					IP = ''.join(str(random.choice(self.iplis)).strip())
					proxy = {'http':IP}
					return self.get(url,timeout,proxy)

		else:
			try:
				IP = ''.join(str(random.choice(self.iplis)).strip())
				proxy = {'http':IP}
				respones = requests.get(url,headers=headers,proxy=proxy,timeout=timeout)
				return respones
			except:
				if num_retries>0:
					time.sleep(5)
					IP = ''.join(str(random.choice(self.iplis)).strip())
					proxy = {'http':IP}
					print(u'正在更换代理，5s后重新获取第',(7-num_retries),u'次')
					print(u'当前代理是：',proxy)
					return self.get(url,timeout,proxy,num_retries-1)
				else:
					print(u'使用代理失败，取消代理')
					return self.get(url,3)