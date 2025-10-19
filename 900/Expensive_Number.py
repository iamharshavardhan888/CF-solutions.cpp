t = int(input())
for _ in range(t):
    s = input()
    length = len(s)
    found_digit = False
    zeros_after = 0

    for i in range(length - 1, -1, -1):
        if s[i] != '0':
            found_digit = True
        elif found_digit:
            zeros_after += 1

    print(length - (zeros_after + 1))
