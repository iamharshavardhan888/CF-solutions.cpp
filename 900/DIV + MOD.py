import math
for _ in range(int(input())):
    l,r,a=map(int,input().split())
    _max=0

    for i in range(r,l-1,-1):
        val=i//a+i%a
        _max=max(_max,val)
        if i%a!=0:
            break

    print(_max)
