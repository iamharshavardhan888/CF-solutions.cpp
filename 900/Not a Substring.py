for _ in range(int(input())):
    s=input()
    n=len(s)

    res1=""
    res2=""

    for i in range(2*n):
        res1+="()"[i&1]
        res2+=")("[i<n]

    if s not in res1:
        print("YES")
        print(res1)
    elif s not in res2:
        print("YES")
        print(res2)
    else:
        print("NO")
