for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    pre_sum = []

    _max = b[0]
    for i in range(1, n):
        _max = max(_max, b[i])
        b[i] = _max

    pre_sum = [a[0]]
    for i in range(1, n):
        pre_sum.append(pre_sum[-1] + a[i])

    if (n >= k):
        ans = pre_sum[k - 1]
        for i in range(k - 2, -1, -1):
            ans = max(ans, pre_sum[i] + (k - 1 - i) * b[i])
        print(ans)
    else:
        remain = k - 1
        ans = [a[0] + b[0] * remain]
        for i in range(1, n):
            remain -= 1
            ans.append(pre_sum[i] + b[i] * remain)
        print(max(ans))

        

        
