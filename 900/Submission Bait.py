for _ in range(int(input())):
    
    n = int(input())

    nums = list(map(int,input().split()))


    freq={}

    for num in nums:
        freq[num]=freq.get(num,0)+1
    
    keys = list(freq.keys())
    keys.sort()

    for key in keys[::-1]:
        if freq[key]%2!=0:
            print("YES")
            break
    else:
        print("NO")