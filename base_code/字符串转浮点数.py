# -*- coding: utf-8 -*-

from functools import reduce

def str2float(s):
    L = list(map(lambda x:x, s)) #把字符串单独取出来

    symbol = 1
    if L[0] == '-':
        symbol = -1
        del L[0]
    elif L[0] == '+':
        symbol = 1
        del L[0]

    S = [x for x in L if x != '.'] # 把小数点取出来
    S1 = list(map(int, S))        #把字符串转化为int型

    def fn(j,k):
        return j*10+k

    num = reduce(fn, S1)

    for i,value in enumerate(reversed(L)):
        if value == '.':
            break

    return num/(10**i) * symbol

print(str2float('123.456'))
print(str2float('12333.4'))
print(str2float('-123.4506'))

print(str2float('+0.4506'))
print(str2float('-0.456'))