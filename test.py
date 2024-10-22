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