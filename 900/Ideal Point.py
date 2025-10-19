for _ in range(int(input())):
    n,k=map(int,input().split())
    x=0
    y=0

    

    for i in range(n):
        l,r=map(int,input().split())

        if (k==l) :
            x+=1
        if (k==r) :
            y+=1

    if (x>0 and y>0):
        print("YES")
    else:
        print("NO")
