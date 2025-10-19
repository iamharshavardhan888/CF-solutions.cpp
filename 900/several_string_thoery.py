def solve():
    n, k = map(int, input().split())
    s = input()
    t = s[::-1]

    if s < t:
        print("YES")
        return

    cnt = 0
    c = s[0]
    for i in range(1, n):
        if s[i] == c:
            cnt += 1

    if cnt == (n - 1):
        print("NO")
        return

    if k == 0:
        print("NO")
        return

    print("YES")

# ✅ Run solve() for each test case
t = int(input())
for _ in range(t):
    solve()
