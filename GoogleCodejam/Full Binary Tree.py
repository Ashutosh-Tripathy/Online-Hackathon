f = open('B-small-practice.in', 'r')
# T = int(f.readline())
# for t in range(T):
#     print("Case #%d: " % (t+1), end = '')
#     edge = {}
#     N = int(f.readline())
#     for i in range(1, N + 1):
#         edge[i] = []
#     for i in range(N - 1):
#         pair = [int(x) for x in f.readline().split()]
#         edge[pair[0]].append(pair[1])
#         edge[pair[1]].append(pair[0])

#     mincount = N
#     for i in range(1, N + 1):
#         if len(edge[i]) in (1, 3):
#             continue
#         else:
#             visited = set()
#             nodes = [i]
#             while True:
#                 child = []
#                 for node in nodes:
#                     if node in visited:
#                         continue
#                     visited.add(node)
#                     temp = list(edge[node])
#                     if len(temp) > 2 or node == i:
#                         # visited = visited.union(temp)
#                         child += temp
#                 if len(child) == 0: break
#                 nodes = child
#             mincount = min(N - len(visited), mincount)
#     print(mincount)










#!/usr/bin/python

from sys import stdin, stderr

def line():
    return map( int, f.readline().strip().split() )

T, = line()

for T in range(1,T+1):
    N, = line()
    V = [ [] for i in range(N) ]

    for i in range(N-1):
        a,b = line()
        V[a-1].append(b-1)
        V[b-1].append(a-1)

    best = 1
    for root in range(N):
        Q = [root]
        P = [x for x in range(N)]
        P[root] = None

        for v in Q:
            for u in V[v]:
                if u != P[v]:
                    Q.append(u)
                    P[u] = v

        Q.reverse()
        A = [ [] for i in range(N) ]

        for v in Q:
            val = 1
            if len(A[v]) >= 2:
                A[v].sort()
                val = sum(A[v][-2:])+1

            if P[v] != None:
                A[P[v]].append(val)
            else:
                if val > best:
                    best = val

    print ('Case #%d: %d' % (T, N-best))
    # print >>stderr, 'Case #%d: %d' % (T, N-best)





