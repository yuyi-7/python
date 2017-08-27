#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module ' #每个模块第一个字符串是注释

__author__ = 'Michael Liao' #作者名

import sys #引入模块

def test():
    args = sys.argv #扫描外部参数的组而sys.argv[0]是文本的地址，后面的元素是外部参数
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()