

for _ in range(int(input())):
    n,m,k=map(int,input().split())

    p=[i for i in range(1,n+1)]

    for num in p[m:][::-1]+p[:m]:
        print(num,end=' ')
    print()