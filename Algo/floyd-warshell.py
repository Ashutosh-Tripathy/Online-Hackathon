from collections import defaultdict
from heapq import *
import random
import math
# edges = []
# for i in range (1000):
#     for j in range(i + 1, 1000):
#         if i != j:
#             edges.append((i,j, random.randrange(100, 1000)))
edges = [
        (1, 4, 10),
        (1, 2, 1),
        (2, 3, 2),
        (4, 3, 3),
        # (1, 2, 1),
        # (1, 4, 2),
        # # (1, 3, 1),
        # (2, 4, 9),
        # (2, 4, 7),
        # (3, 4, 4),
        # (4, 4, 15),
        # (4, 6, 6),
        # (4, 6, 8),
        # (4, 7, 9),
        # (6, 7, 11)
    ]
def floyed_warshell(g):
    nodes = set([1,2,3,4])
    edges = [[math.inf for x in range(len(nodes))] for y in range(len(nodes))]
    print(edges)
    for start, end, cost in g:
        edges[start-1][end-1] = cost
        edges[end-1][start-1] = cost


    for i in nodes:
        for j in nodes:
            for k in nodes:
                if j != k:
                    if edges[j-1][k-1] > edges[j-1][i-1] + edges[k-1][i-1]:
                        print(edges)
                    edges[j-1][k-1] = min(edges[j-1][k-1], edges[j-1][i-1] + edges[k-1][i-1])
                else:
                    edges[j-1][k-1] = 0

    print(edges)
floyed_warshell(edges)