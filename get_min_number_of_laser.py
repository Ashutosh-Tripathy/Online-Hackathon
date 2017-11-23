from __future__ import division
from math import atan2


class Point2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
  # library with types used in the task


def solution(A):
    # write your code in Python 2.7
    slope_set = set()
    for a in A:
        slope = (atan2(a.y, a.x))
        if slope not in slope_set:
            slope_set.add(slope)
    print(slope)
    return len(slope)


arr = [(3, 0), (-3, 0), (5, 0), (-5, 0), (0, 3),
       (0, 5), (0, -3), (0, -5), (2, 2), (3, 2)]
arr = [Point2D(z[0], z[1]) for z in arr]
print(solution(arr))