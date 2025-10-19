for _ in range(int(input())):
    n=int(input())
    if n%2==0:
        ans=[1,3]
        extra=[2 for i in range(n-2)]
        ans.extend(extra)
        for num in ans:
            print(num,end=' ')
        print()
    else:
        for i in range(n):
            print(1,end=' ')
        print()