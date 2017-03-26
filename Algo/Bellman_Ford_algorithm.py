import math
edges = [
        (1, 2, 4),
        (1, 4, 2),
        (1, 3, 1),
        (2, 7, 3),
        (3, 7, 1),
        (3, 5, 2),
        (4, 5, 1),
        (5, 6, 1),
        (6, 7, 1),
        (6, 2, 1)
    ]

def bellman_ford():
    nodes = {1, 2, 3, 4, 5, 6, 7}
    distance = {x:math.inf for x in nodes}
    start = 1
    distance[1] = 0
    for i in range(len(nodes)):
        for u, v, w in edges:
            distance[v] = distance[u] +w if distance[v] > distance[u] + w else distance[v]
            print(distance)

bellman_ford()