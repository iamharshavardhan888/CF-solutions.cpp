for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))


    sum = max(a[0], 0)
    ans = sum
    ive = 0
    for i in range(1, n):
        if a[i] < 0:
            ive += 1
        if ((abs(a[i]) ^ abs(a[i - 1])) & 1):
            if sum < 0: 
                sum = a[i]
            else:
                sum += a[i]
        else:
            sum = a[i]

        ans = max(ans, sum)
        
    if ive == n - 1 and a[0] < 0:
        ans = max(a)
    
    print(ans)
            
        


        