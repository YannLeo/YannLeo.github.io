N, V = map(int, input().split())
dp = [0]*(V+1)

for _ in range(N):
    s = int(input())
    vs, ws = [], []
    for _ in range(s):
        v, w = map(int, input().split())
        vs.append(v); ws.append(w)
    for j in range(V, 0, -1):
        for v, w in zip(vs, ws):
            if j >= v: dp[j] = max(dp[j], dp[j-v]+w)
print(dp[-1])