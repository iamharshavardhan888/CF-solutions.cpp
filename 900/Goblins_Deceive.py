def max_subsequence(s,n):
    u_c=s.count('_')
    d_c=s.count('-')
    if (n<3 or u_c<1 or d_c<2):
        return 0
    d1=d_c//2
    d2=d_c-d1
    
    return d1*u_c*d2


t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    print(max_subsequence(s,n))