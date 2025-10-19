for _ in range(int(input())):

    n,H,M=map(int,input().split())
    l=[]

    for __ in range(n):
        l.append(list(map(int,input().split())))

    l.sort()

    
    for i in range(n):
        if l[i][0]==H and l[i][0]>=M or (l[i][0]>H):
            break

    if H>l[i][0]:
        ans_h=24-H+l[i][0]
    else:
        ans_h=l[i][0]-H
    
    ans_m=l[i][1]-M

    if ans_m<0:
        ans_h-=1
        ans_m+=60
    
    print(ans_h,ans_m)


