for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    frq = {}
    p = a.copy()
    a.sort()
    pre = [a[0]]
    for i in range(1, n):
        pre.append(pre[-1] + a[i])

    for i in range(n):
        sum = pre[i]
        cnt = 0 
        for j in range(i + 1, n):
            if sum >= a[j]:
                sum += a[j]
                cnt += 1
            else:
                break
        frq[a[i]] = cnt + i
    
    for i in range(n):
        print(frq[p[i]], end = ' ')

    print()
