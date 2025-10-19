t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    p=[0] * n
    index=k-1
    element=1
    while index<n:
        p[index]=element
        element+=1
        index+=k
    for i in range(n):
        if p[i]==0:
            p[i]=element
            element+=1
        print(p[i],end=' ')

            

