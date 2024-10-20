import collections

def spfa(graph, start):
    """
    :param graph: 图的邻接表示，graph[u]表示用户顶点u相连的边和权重
    :param start: 起点
    :return: 从起点到其他顶点的最短距离
    """
    # 初始化距离
    distance = {vertex: float('inf') for vertex in graph}
    distance[start] = 0

    # 初始化队列
    queue = collections.deque([start])

    # 记录每个顶点的入队次数，防止出现负环
    visit_count = {vertex: 0 for vertex in graph}
    visit_count[start] = 0
    
    # SPFA算法
    while queue:
        vertex = queue.popleft()
        for neighbor, weight in graph[vertex].items():
            new_distance = distance[vertex] + weight
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                visit_count[neighbor] += 1
                if visit_count[neighbor] > len(graph):
                    print('存在负环')
                    return False
                queue.append(neighbor)
    return distance



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
dis = spfa(graph, v0)
print(dis)