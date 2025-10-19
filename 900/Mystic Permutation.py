for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))

    if n==1:
        print(-1)
        continue

    torf=[]

    for i in range(1,n+1):
        if l[i-1]==i:
            torf.append(True)
        else:
            torf.append(False)

    #modifiying to lexicologically smaller

    p=[i for i in range(1,n+1)]

    for i in range(n-1):
        if torf[i]:
            p[i],p[i+1]=p[i+1],p[i]
            torf[i],torf[i+1]=False,False
    
    if torf[-1]:
        p[-1],p[-2]=p[-2],p[-1]

    for num in p:
        print(num,end=' ')
    print()
    