for _ in range(int(input())):
    n = int(input())
    s = "aeiou"
    mul=n//5
    exces=n%5
    res=""
    for __ in range(mul):
        res+=s
    for i in range(exces):
        res+=s[i]
    
    print(''.join(sorted(list(res))))