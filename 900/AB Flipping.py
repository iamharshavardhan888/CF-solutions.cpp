for _ in range(int(input())):
    n=int(input())
    s=input()
    
    k=n-1
    while s[k]=='A':
        chr=s[k]

        if k<0 or chr=='B':
            break
        else :
            k-=1

    op=0
    if k<0:
        print(0)
        continue

    
    lastA=k
    for i in range(k,-1,-1):
        chr=s[i]

        if chr == 'A' :
            op+=(lastA-i)
            lastA=i
        
    print(op)
