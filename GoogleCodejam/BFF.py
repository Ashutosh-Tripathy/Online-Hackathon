
'''
Created on Dec 18, 2016

@author: tripathy
'''
# P R S

with open('B-small-practice.in') as f:
    content = f.readlines()
import copy

# def create_graph():
#     global BFF
#     BFF = [int(x) for x in content.pop(0).split()]
#     global graph
#     graph = {}
#     for number in range(N):
#         if not number + 1 in graph:
#             graph[number + 1] = set()
#         if not BFF[number] in graph:
#             graph[BFF[number]] = set()
#         graph[number + 1].add(BFF[number])
#         graph[BFF[number]].add(number + 1)
#     # print(graph)

# def get_max_count_starting_node(item, path_traversed, current_count):
#     if (item in path_traversed):
#         return current_count
#     path_traversed.add(item)
#     current_count += 1
#     max_local_count = current_count
#     for node in graph[item]:
#         if ((len(path_traversed) != 0 and (BFF[item - 1] in path_traversed)) or (node == BFF[item - 1])):
#             count = get_max_count_starting_node(node, path_traversed, current_count)
#             max_local_count = max(max_local_count, count)
#     return max_local_count


# def get_max_circle_count():
#     max_count = 0
#     for item in graph:
#         path_traversed, current_count = set(), 0
#         result = get_max_count_starting_node(item, path_traversed, current_count)
#         max_count = max(max_count, result)
#     return max_count

pair_max = {}

def update_pair_max(pprev, size):
    if pprev in pair_max:
        pair_max[pprev] = max(pair_max[pprev], size)
    else:
        pair_max[pprev] = size

def get_max_path_size(start_node, size):
    size, path_traversed = 0, set()
    prev = -1 , pprev = 1, current = start_node
    while True:
        if (current in bff_map):
            new_node = bff_map[current]
            if (new_node in path_traversed):
                if (new_node == start_node):
                    if (size == 2):
                        return 0
                    else:
                        return size
                else:
                    return 0
            else:
                path_traversed.add(new_node)
                pprev = prev
                prev = current
                current = new_node
            size += 1
        else:
            return size


def get_max_circle_count():
    max_count = 0
    for bff in BFF:
        size = 0
        max_count = max(get_max_path_size(bff, size), max_count)



def create_bff_map():
    BFF = [int(x) for x in content.pop(0).split()]
    global bff_map
    bff_map = {}
    for i in range(N):
        bff_map[i + 1] = BFF[i]


number_of_test_cases, bff_map = int(content.pop(0)), {}
for y in range(number_of_test_cases):
    N = int(content.pop(0))
    create_bff_map()
    result = get_max_circle_count()
    print("Case #"+str(y+1)+": " + str(result))
