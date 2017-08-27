#输出类似323,9889,这样的回数
#print(list(filter((lambda n:str(n)==str(n)[::-1]), range(1, 10000))))
'''
def is_palindrome(n):
    n=str(n)
    def ff(k):
        a=''
        for x in reversed(k):
            a+=x
        return a
    return n==ff(n)

output=filter(is_palindrome,range(1,1000))
print(list(output))
'''
def sushu(n):
	y=str(n)
	a=''
	for x in reversed(y):
		a+=x
	return str(n)==a
output=filter(sushu,range(1,1000))
print(list(output))
