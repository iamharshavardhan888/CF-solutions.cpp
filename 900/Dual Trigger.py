for _ in range(int(input())):
    n=int(input())

    s=input()

    ones=s.count('1')

    if ones%2!=0:
        print("NO")
    elif ones==2:

        for i in range(1,n):
            if s[i]==s[i-1]=="1":
                print("NO")
                break
        else:
            print("YES")
    else:
        print("YES")