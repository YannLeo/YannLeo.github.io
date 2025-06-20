# 多重背包

有 N 种物品和一个容量是 $V$ 的背包。**第 $i$ 种物品最多有 $s_i$ 件**，每件体积是 $v_i$ ，价值是 $w_i$ 。求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。输出最大价值。

## 分析

$N$ 件物品，背包容量 $V$，每件使用次数 $s_i$ 次。
数组存入物品的体积和价值和使用次数 ：体积 $v[i]$, 价值 $w[i]$，使用次数 $s[i],i = 0 , 1 , 2 , . . . , N − 1 , N$

**定义状态**：$f[i][j]$, 代表前i个物品，存入容量为j的背包里的最大价值。

$状态转移$：$ f[i][j] = \max{(f[i-1][j-k*v[i]] + k*w[i])}, k=0,1,...,\min(s_i, j//v[i])$。
$k$ 的范围代表，第 $i$ 个物品取的次数。上限不能超过当前背包的容量,也不能超过题目限制的使用次数。

边界：$f[0] = [0,0,0...,0]$

$result = f[N][V]$


=== "🔵 Python"
    ```python
    N,V = map(int, input().split())

    v = [0] * (N+1)
    w = [0] * (N+1)
    s = [0] * (N+1)

    for i in range(1, N+1):
        v[i], w[i], s[i] = map(int, input().split())
        
        
    f = [0] *(V+1)

    for i in range(1, N+1):
        for j in range(V,v[i]-1,-1):
            for k in range(1, min(s[i], j//v[i])+1):
                f[j] = max(f[j], f[j-k*v[i]]+k*w[i])
                
    print(f[V])



    ```

=== "🔴 C++"
    ```
    comming soon
    ```
