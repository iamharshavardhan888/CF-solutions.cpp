for _ in range(int(input())):

    a,b,c,d=map(int,input().split())
    res=""

    for i in range (1,13):
        if i==a or i==b:
            res+="a"
        elif i==c or i==d:
            res+="b"
    if res=="abab" or res=="baba":
        print("YES")
    else:
        print("NO")