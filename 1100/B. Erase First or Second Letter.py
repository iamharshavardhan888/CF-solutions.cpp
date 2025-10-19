for _ in range(int(input())):
    n = int(input())
    s = input()
    se = set()
    se.add(s[0])
    ans = 1

    for i in range(1, n):
        se.add(s[i])
        ans += (len(se))
    
    print(ans)
    







