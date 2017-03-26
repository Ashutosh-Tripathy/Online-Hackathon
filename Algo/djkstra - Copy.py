from collections import defaultdict
from heapq import *
import random

edges = []
for i in range (1000):
    for j in range(i + 1, 1000):
        if i != j:
            edges.append((i,j, random.randrange(100, 1000)))

def djkestra(start, end, g):
    if start == end:
        return 0
    edges = defaultdict(list)
    for node1, node2, cost in g:
        edges[node1].append((node2, cost))

    heap = []
    path, seen = (), set()
    heap.append((0, start, path))
    while heap:
        (cost, node, path) = heappop(heap)
        if node not in seen:
            seen.add(node)
            path += (node,)
            if node == end:
                print(counter)
                return (cost, path)
            for node2, ct in edges.get(node, ()):
                if node2 not in seen:
                    heappush(heap, (cost + ct, node2, path))
print(djkestra(1, 997, edges))
print(maxheap)