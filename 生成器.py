def tri():
    L=[1]
    yield L
    while True:
        L=[1]+[L[x]+L[x+1] for x in range(len(L)-1)]+[1]
        yield L

n=0
for L in tri():
    print(L)
    n=n+1
    if n==10:
        break
#L(x*x for x in range(10))也是生成器一种创建方法，上面是函数创建方法