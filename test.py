def kmp(s, t):
    if not t: return 0
    pi = [0] * len(t)
    j = 0
    for i in range(1, len(t)):
        while j > 0 and t[i] != t[j]:
            j = pi[j-1]
        if t[i] == t[j]:
            j += 1
        pi[i] = j

    j = 0
    for i, c in enumerate(s):
        while j > 0 and t[j] != c:
            j = pi[j-1]
        if t[j] == c:
            j += 1
        if j == len(t):
            return i - j + 1

    return -1

if __name__ == '__main__':
    text = "abababaabc"
    pattern = "ababaab"
    res = kmp(text, pattern)
    print(res)