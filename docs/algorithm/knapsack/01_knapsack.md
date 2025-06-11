# 01背包

有 $N$ 件物品和一个容量是 $V$ 的背包。每件物品只能使用一次。第 $i$ 件物品的体积是 $v_i$ ，价值是 $w_i$ 。求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。输出最大价值。

## 分析

$N$ 件物品 ， 背包容量 $V$， 每件只能使用一次。
数组存入物品的体积和价值：体积 $v[i]$ , 价值 $w[i],i = 0 , 1 , 2 , . . . , N − 1$ 。

**定义状态**：$f[i][j]$, 代表前 $i$ 个物品，存入容量为 $j$ 的背包里的最大价值。

**状态转移**：$f[i][j] = \max{(f[i-1][j],f[i-1][j-v[i]] + w[i])}$

- 不取第i个物品： $ f[i][j] = f[i-1][j]$
- 取第i个物品：$f[i][j] = f[i-1][j-v[i]] + w[i]$

**边界**：$f[0] = [0,0,0...,0]$

$result = f[N][V]$



## 代码

=== "🔵 Python"
    ```python
    N, V = map(int, input().split())  # 物品数， 背包容量

    v = [0] * (N + 1)  # 体积 索引从1开始到n
    w = [0] * (N + 1)  # 价值 索引从1开始到n

    for i in range(1, N + 1):
        v[i], w[i] = map(int, input().split())

    f = [[0 for i in range(V+1)] for i in range(N+1)]  # 初始化全0

    for i in range(1, N + 1):
        for j in range(V + 1):
            f[i][j] = f[i - 1][j]

            if j >= v[i]:
                f[i][j] = max(f[i][j], f[i - 1][j - v[i]] + w[i])


    print(f[N][V])

    # 输入样例
    # 4 5
    # 1 2
    # 2 4
    # 3 4
    # 4 5

    # 输出样例：
    # 10

    ```

=== "🔴 C++"
    ```
    comming soon
    ```

以上的二维DP可以简化为一维DP，以减小空间复杂度


=== "🔵 Python"
    ```python
    N, V = map(int, input().split())  # 物品数， 背包容量

    v = [0] * (N + 1)  # 体积 索引从1开始到n
    w = [0] * (N + 1)  # 价值 索引从1开始到n

    for i in range(1, N + 1):
        v[i], w[i] = map(int, input().split())

    f = [0 for i in range(V+1)]  # 初始化全0

    for i in range(1, N + 1):
        for j in range(V,v[i]-1,-1):
                f[j] = max(f[j], f[j - v[i]] + w[i])

    print(f[V])

    ```