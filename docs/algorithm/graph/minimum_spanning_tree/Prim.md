# Prim

Prim算法是用于寻找加权无向图的最小生成树的经典贪心算法。与Kruskal算法不同，Prim算法是逐步扩展生成树，每次从当前生成树中选择一条权重最小的边连接一个新顶点。

Prim算法从图中的一个顶点开始，逐步扩展最小生成树。在每一步中，从已加入的生成树的顶点集合中，选择一条连接到未加入顶点的权重最小的边，直到所有顶点都被加入到生成树中。

## 代码

=== "🔵 Python"
    ```python
    import heapq

    def prim(graph, start):
        min_spanning_tree = []
        visited = set()
        priority_queue = [(0, -1, start)]
        heapq.heapify(priority_queue)

        while priority_queue:
            weight, father, node = heapq.heappop(priority_queue)
            if node not in visited:
                visited.add(node)
                min_spanning_tree.append((weight, father, node))

                for neighbor, neighbor_weight in graph[node].items():
                    if neighbor not in visited:
                        heapq.heappush(priority_queue, (neighbor_weight, node, neighbor))

        return min_spanning_tree


    graph = {
        'A': {'B': 1, 'D': 4},
        'B': {'A': 1, 'C': 2, 'E': 3},
        'C': {'B': 2, 'F': 5},
        'D': {'A': 4, 'E': 1},
        'E': {'B': 3, 'D': 1, 'F': 2},
        'F': {'C': 5, 'E': 2}
    }

    print("Prim算法最小生成树：", prim(graph, 'A'))
    ```

=== "🔴 C++"
    ``C++     comming soon     ``
