# Bellman-Ford算法

Bellman-Ford算法是一种用于寻找加权图中单源最短路径的算法。与Dijkstra算法不同，Bellman-Ford算法能够处理带有负权重边的图。算法复杂度为 $O(VE)$.

## 步骤

Bellman-Ford算法的基本思想是通过逐步放松边来更新路径长度。算法会重复进行多次，直到找到最短路径。

1. 初始化图中所有节点的距离值为无穷大（∞），源节点的距离值为0。
2. 对于图中的每一条边，检查是否可以通过该边放松路径。如果可以，则更新目标节点的距离值。
3. 重复执行上述步骤 \(V - 1\) 次，其中 \(V\) 是图中节点的数量。
4. 进行一次额外的循环以检查负权重环。如果可以继续放松某些边，则说明图中存在负权重环。


## 代码

=== "🔵 Python"
    ```python
    # Bellman-Ford核心算法
    # 对于一个包含n个顶点，m条边的图, 计算源点到任意点的最短距离
    # 循环n-1轮，每轮对m条边进行一次松弛操作

    # 定理：
    # 在一个含有n个顶点的图中，任意两点之间的最短路径最多包含n-1条边
    # 最短路径肯定是一个不包含回路的简单路径（回路包括正权回路与负权回路）
    # 1. 如果最短路径中包含正权回路，则去掉这个回路，一定可以得到更短的路径
    # 2. 如果最短路径中包含负权回路，则每多走一次这个回路，路径更短，则不存在最短路径
    # 因此最短路径肯定是一个不包含回路的简单路径，即最多包含n-1条边，所以进行n-1次松弛即可




    def getEdges(G):
        """ 输入图G，返回其边与端点的列表 """
        v1 = []     # 出发点
        v2 = []     # 对应的相邻到达点
        w  = []     # 顶点v1到顶点v2的边的权值
        for i in G:
            for j in G[i]:
                if G[i][j] != 0:
                    w.append(G[i][j])
                    v1.append(i)
                    v2.append(j)
        return v1,v2,w

    class CycleError(Exception):
        pass

    def Bellman_Ford(G, v0, INF=float("inf")):
        v1,v2,w = getEdges(G)

        # 初始化源点与所有点之间的最短距离
        dis = dict((k,INF) for k in G.keys())
        dis[v0] = 0

        # 核心算法
        for k in range(len(G)-1):   # 循环 n-1轮
            check = 0           # 用于标记本轮松弛中dis是否发生更新
            for i in range(len(w)):     # 对每条边进行一次松弛操作
                if dis[v1[i]] + w[i] < dis[v2[i]]:
                    dis[v2[i]] = dis[v1[i]] + w[i]
                    check = 1
            if check == 0: break

        # 检测负权回路
        # 如果在 n-1 次松弛之后，最短路径依然发生变化，则该图必然存在负权回路
        flag = 0
        for i in range(len(w)):             # 对每条边再尝试进行一次松弛操作
            if dis[v1[i]] + w[i] < dis[v2[i]]:
                flag = 1
                break
        if flag == 1:
    #         raise CycleError()
            return False
        return dis




    # 示例图
    graph = {
        'A': {'B': 1, 'D': 4},
        'B': {'A': 1, 'C': 2, 'E': 3},
        'C': {'B': 2, 'F': 5},
        'D': {'A': 4, 'E': 1},
        'E': {'B': 3, 'D': 1, 'F': 2},
        'F': {'C': 5, 'E': 2}
    }

    v0 = 'A'
    dis = Bellman_Ford(graph, v0)
    print(dis)
    ```

=== "🔴 C++"
    ```C++
    comming soon
    ```