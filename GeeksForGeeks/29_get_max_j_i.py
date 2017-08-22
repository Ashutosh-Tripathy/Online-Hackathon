from heapq import *


def get_max_diff():
    items = [6, 5, 4, 3, 2, 1]
    start_heap, end_heap = [], [-items[-1]]
    i, j = 0, len(items) - 2
    counter = 0
    while i <= j:
        if counter == 0:
            heappush(start_heap, items[i])
            if start_heap[0] < abs(end_heap[0]):
                return j - i + 1
            else:
                i += 1
        else:
            heappush(end_heap, -items[j])
            if start_heap[0] < abs(end_heap[0]):
                return j - i + 1
            else:
                j -= 1
        counter = (counter + 1) % 2
    return -1


print(get_max_diff())

