t=int(input())
for _ in range(t):
    n,x=map(int, input().split())
    p=[]
    s={i for i in range(n)}
    for i in s:
        if(i<x):
            p.append(i)
    for i in s:
        if(i>x):
            p.append(i)
    if(x in range(n)):
        p.append(x)
    for i in p:
        print(i,end=' ')