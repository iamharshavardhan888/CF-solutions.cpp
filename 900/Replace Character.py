t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())

    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    if len(freq)==1:
        print(''.join(s))
        continue

    if len(freq) == n:
        s[1] = s[0] 
        print(''.join(s))
        continue

    max_freq_char = max(freq, key=freq.get)
    min_freq_char = min(freq, key=freq.get)

    if(max_freq_char==min_freq_char):
        for key in freq:
            if key!=min_freq_char:
                max_freq_char=key
                break
    


    for i in range(n):
        if s[i] == min_freq_char:
            s[i] = max_freq_char
            break
    print(''.join(s))

    