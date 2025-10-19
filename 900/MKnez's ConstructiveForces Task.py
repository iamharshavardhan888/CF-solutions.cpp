for _ in range(int(input())):
    n=int(input())
 
    
    if n==2:
        print("YES")
        print(1,-1)
        continue
 
    
    if n%2==0 or n>=5:
        print("YES")
        a=n//2-1
        b=(n-n//2)-1
        for i in range(n):
            print([-a,b][i&1],end=' ')
        print()
 
    else:
        print("NO")