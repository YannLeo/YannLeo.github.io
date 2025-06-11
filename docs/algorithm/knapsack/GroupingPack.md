# 分组背包

有 $N$ 组物品和一个容量是 $V$ 的背包。
每组物品有若干个，同一组内的物品最多只能选一个。
每件物品的体积是 $v_{ij}$ ，价值是 $w_{ij}$，其中 $i$ 是组号，$j$ 是组内编号。
求解将哪些物品装入背包，可使物品总体积不超过背包容量，且总价值最大。
输出最大价值。

## 代码

=== "🔵 Python"
    ```python
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

    # 输入样例
    # 3 5     组数 容量
    # 2       第一组物品个数
    # 1 2     物品的容量和价值
    # 2 4
    # 1       第二组
    # 3 4
    # 1       第三组
    # 4 5
    ```