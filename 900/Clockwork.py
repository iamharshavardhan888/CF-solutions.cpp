for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    
    for i in range(n):
        if a[i]<=2*max(i,n-i-1):
            print("NO")
            break
    else:
        print("YES")