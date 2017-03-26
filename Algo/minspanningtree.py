# from UnionFind import *
from collections import defaultdict
from unionfind import *
# edges = []
# for i in range (1000):
#     for j in range(i + 1, 1000):
#         if i != j:
#             edges.append((i,j, random.randrange(100, 1000)))

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

def min_span_tree(g):

    edges = defaultdict(dict)
    for node1, node2, cost in g:
        edges[node1][node2] = cost
        edges[node2][node1] = cost

    tree, visited = [], set()
    for item, u, v in sorted((edges[u][v], u, v) for u in edges for v in edges[u]):
        if visited.union([u, v]) == visited:
            continue
        tree.append((u,v))
        visited = visited.union([u,v])
    return tree
print (min_span_tree(edges))


# # from UnionFind import *
# from collections import defaultdict
# from unionfind import *
# # edges = []
# # for i in range (1000):
# #     for j in range(i + 1, 1000):
# #         if i != j:
# #             edges.append((i,j, random.randrange(100, 1000)))

# edges = [
#         (1, 2, 4),
#         (1, 4, 2),
#         (1, 3, 1),
#         (2, 7, 3),
#         (3, 7, 1),
#         (3, 5, 2),
#         (4, 5, 1),
#         (5, 6, 1),
#         (6, 7, 1)
#     ]

# def min_span_tree(g):

#     edges = dict()
#     for node1, node2, cost in g:
#         if node1 not in edges:
#             edges[node1] = dict()
#         if node2 not in edges:
#             edges[node2] = dict()
#         edges[node1][node2] = cost
#         edges[node2][node1] = cost

#     subtree, tree = unionfind(7), []

#     for item in sorted((edges[u][v], u, v) for u in edges for v in edges[u]):
#         if subtree[u] != subtree[v]:
#             tree.append((u,v))
#             subtree.union(u,v)
#     return tree
# print (min_span_tree(edges))

