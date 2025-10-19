for _ in range(int(input())):

    y1,x1=map(int,input().split())
    y2,x2=map(int,input().split())
    y3,x3=map(int,input().split())

    y_path=0
    x_path=0

    if (y1-y2)*(y1-y3)>=0:
        y_path=min(abs(y1-y2),abs(y1-y3))
        

    if (x1-x2)*(x1-x3)>=0:
        x_path=min(abs(x1-x2),abs(x1-x3))

    print(x_path+y_path+1)

