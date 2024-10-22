# Kruskal

Kruskal算法通过将图中的边按权重从小到大排序，然后依次将边加入到生成树中，直到生成树中包含所有顶点或边的数量达到 `V-1`（ `V` 为顶点数）。在加入边时，若加入该边会形成环，则不选择该边。

一般通过并查集实现

## 代码

=== "🔵 Python"
    ```python
    def find(parent, node):
        if parent[node] != node:
            parent[node] = find(parent, parent[node])
        return parent[node]

    def union(parent, rank, node1, node2):
        root1 = find(parent, node1)
        root2 = find(parent, node2)

        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1

    def kruskal(graph):
        min_spanning_tree = []
        edges = []

        for node, neighbors in graph.items():
            for neighbor, weight in neighbors.items():
                edges.append((weight, node, neighbor))

        edges.sort()

        parent = {node: node for node in graph}
        rank = {node: 0 for node in graph}

        for edge in edges:
            weight, node1, node2 = edge
            if find(parent, node1) != find(parent, node2):
                union(parent, rank, node1, node2)
                min_spanning_tree.append((weight, node1, node2))

        return min_spanning_tree


    graph = {
        'A': {'B': 1, 'D': 4},
        'B': {'A': 1, 'C': 2, 'E': 3},
        'C': {'B': 2, 'F': 5},
        'D': {'A': 4, 'E': 1},
        'E': {'B': 3, 'D': 1, 'F': 2},
        'F': {'C': 5, 'E': 2}
    }

    print("Kruskal算法最小生成树：", kruskal(graph))
    ```

=== "🔴 C++"
    ```C++
    comming soon
    ```