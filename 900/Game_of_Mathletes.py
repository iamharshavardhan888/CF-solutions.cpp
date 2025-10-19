t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    freq = [0] * (2 * n + 2)

    for x in arr:
        freq[x] += 1

    score = 0

    for a in range(1, (k // 2) + 1):
        b = k - a
        if a == b:
            score += freq[a] // 2
        elif freq[a] > 0 and freq[b] > 0:
            score += min(freq[a], freq[b])
            freq[a] = 0
            freq[b] = 0

    print(score)
