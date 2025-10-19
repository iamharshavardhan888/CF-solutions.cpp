for _ in range(int(input())):
    n=int(input())
    s=input()

    if n==1 or s.count('1')==0:
        print(0)
        continue

    cntpair_1=0
    group=False

    for i in range(n):
        if s[i]=='1':
            if not group:
                cntpair_1+=1
                group=True
        else:
            group=False


    if s[-1]=='1':
        print(2*(cntpair_1-1))
    else:
        print(2*cntpair_1-1)
    
