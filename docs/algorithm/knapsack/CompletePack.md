# 完全背包

有 $N$ 件物品和一个容量是 $V$ 的背包。**每件物品使用次数不限**。第 $i$ 件物品的体积是 $v_i$，价值是 $w_i$。求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。输出最大价值。

## 分析

$N$ 件物品 ， 背包容量 $V$， 每件使用次数不限。
数组存入物品的体积和价值：体积 $v[i]$, 价值 $w[i], i = 0 , 1 , 2 , . . . , N − 1 , N$。

**定义状态**：$f[i][j]$, 代表前 $i$ 个物品，存入容量为 $j$ 的背包里的最大价值。

**状态转移**： $f[i][j] = \max{(f[i-1][j-k*v[i]] + k*w[i])}, i=0,1,...,j//v[i]$。
k的范围代表，第i个物品取的次数。上限不能超过当前背包的容量。

**边界**：$f[0] = [0,0,0...,0]$

$result = f[N][V]$

## 代码

=== "🔵 Python"
    ```python
    N, V = map(int, input().split())

    v = [0] * (N + 1)
    w = [0] * (N + 1)

    for i in range(1, N + 1):
        v[i], w[i] = map(int, input().split())


    f = [[0 for i in range(V+1)] for i in range(N+1)]  # 初始化全0

    for i in range(1, N + 1):
        for j in range(V + 1):
            f[i][j] = f[i - 1][j]
            for k in range(1, j // v[i] + 1):
                f[i][j] = max(f[i][j], f[i - 1][j - k * v[i]] + k * w[i])

    print(f[N][V])

    ```

=== "🔴 C++"
    ```
    comming soon
    ```

以上的二维DP可以简化为一维DP，以减小空间复杂度


=== "🔵 Python"
    ```python
    N, V = map(int, input().split())

    v = [0] * (N + 1)
    w = [0] * (N + 1)

    for i in range(1, N + 1):
        v[i], w[i] = map(int, input().split())

    f = [0 for i in range(V+1)]  # 初始化全0

    for i in range(1, N + 1):
        for j in range(V, v[i]-1, -1):
            for k in range(0, j // v[i] + 1):
                f[j] = max(f[j], f[j - k * v[i]] + k * w[i])

    print(f[V])


    ```

可以继续省略取物品次数k的等价转换代码

=== "🔵 Python"
    ```python
    N, V = map(int, input().split())

    v = [0] * (N + 1)
    w = [0] * (N + 1)

    for i in range(1, N + 1):
        v[i], w[i] = map(int, input().split())

    f = [0 for i in range(V+1)]  # 初始化全0

    for i in range(1, N + 1):
        for j in range(v[i], V+1):
                f[j] = max(f[j], f[j-v[i]] + w[i])

    print(f[V])

    ```