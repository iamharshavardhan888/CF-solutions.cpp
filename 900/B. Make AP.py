for _ in range(int(input())):

    x,y,z=map(int,input().split())

    if ((x+z)/2)%y==0 or (2*y-x)%z==0:
        print("YES")
    else:
        print("NO")