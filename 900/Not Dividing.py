for _ in range(int(input())):
    n=int(input())

    l=list(map(int,input().split()))


    for i in range(n):
        if l[i]==1:
            l[i]+=1


    for i in range(1,n):
        if l[i]%l[i-1]==0:
            l[i]+=1

    for num in l:
        print(num,end=' ')
        
    print()
        




