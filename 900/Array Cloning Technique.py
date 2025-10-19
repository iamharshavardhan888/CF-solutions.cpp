from collections import Counter
for _ in range(int(input())):
    n=int(input())
    nums=list(map(int,input().split()))


    freq = Counter(nums)
    max_rep=max(freq.values())

    op=0

    while max_rep<n:
        op+=1

        if 2*max_rep<n:
            op+=max_rep
            max_rep*=2
        else:
            op+=(n-max_rep)
            max_rep=n
    
    print(op)
