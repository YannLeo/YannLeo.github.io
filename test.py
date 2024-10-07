import heapq

def dijkstra(graph, start):
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return distances, previous_nodes

# 示例图
graph = {
    'A': {'B': 1, 'D': 4},
    'B': {'A': 1, 'C': 2, 'E': 3},
    'C': {'B': 2, 'F': 5},
    'D': {'A': 4, 'E': 1},
    'E': {'B': 3, 'D': 1, 'F': 2},
    'F': {'C': 5, 'E': 2}
}

distances, previous_nodes = dijkstra(graph, 'A')
print("Distances:", distances)
print("Previous Nodes:", previous_nodes)