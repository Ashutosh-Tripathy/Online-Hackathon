
'''
Created on Dec 18, 2016

@author: tripathy
'''

import copy
import math

with open('C-small-practice.in') as f:
    content = f.readlines()

def get_distance(start_point, end_point):
    return math.sqrt(pow(end_point[0] - start_point[0], 2) + pow(end_point[1] - start_point[1], 2) + pow(end_point[2] - start_point[2], 2))


def get_min_distance(N, T, P, V):

    start_point = P[0]
    end_point = P[1]

    D = get_distance(start_point, end_point)
    nodes = [0]
    distance_map = {0 : 0, 1 : D}
    while (len(nodes) > 0):
        new_nodes = []
                
        for node in nodes:
            for i in range(len(P)):
                D = min(D, distance_map[1])
                if not (i == node or i == 0 or node == 1):
                    distance = get_distance(P[node], P[i])
                    if (distance < D):
                        if i in distance_map:
                            distance_map[i] = max(distance, distance_map[node])
                        else:
                            distance_map[i] = distance
                            
                        new_nodes.append(i)
#                 print(nodes)
#                 print(new_nodes)
#                 print(distance_map)
#                 print(i)
#                 print(D)
#                 input()
                
        # print(new_nodes)
        nodes = new_nodes
    return distance_map[1]

T = int(content.pop(0))
for x in range(T):
    P, Z, V = [], [], []
    N, T = [int(y) for y in content.pop(0).split()]
    for i in range(N):
        Z = [int(x) for x in content.pop(0).split()]
        P.append(Z[:int(len(Z)/2)])
        V.append(Z[int(len(Z)/2):])
    print("Case #"+str(x+1)+": " + str(get_min_distance(N, T, P, V)))


