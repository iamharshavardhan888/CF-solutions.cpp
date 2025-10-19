t=int(input())
for _ in range(t):
    n=int(input())
    if n%2==0:
        print((n-2)*'3'+'66')
    elif n==1 or n==3:
        print(-1)
    elif n%2!=0:
        print((n-5)*'3'+'36366')
    else:
        print(-1)
