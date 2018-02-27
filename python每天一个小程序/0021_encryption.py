#!/usr/bin/env python
# encoding: utf-8

'第 0021 题： 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。'

import hashlib
from collections import defaultdict
bd = {}
bd = defaultdict(lambda:'N/A')

def get_mad5(password):
	a = hashlib.md5()  #hashlib.sha1()
	a.update(password.encode('utf-8'))
	return a.hexdigest()

def register(username,password):
	bd[username] = get_mad5(password+username+'SALT')

def login(username,password):
	b = get_mad5(password+username+'SALT')
	if b == bd[username]:
		return True
	else:
		return False

a = input('注册用户名：')
b = input('注册密码：')
register(a,b)
print(get_mad5(a+b+'SALT'))
a = input('登录用户名：')
b = input('登录密码：')
print(login(a,b))