class Point2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
  # library with types used in the task


def get_sign(x):
    return "+" if x >= 0 else "-"


def solution(A):
    # write your code in Python 2.7
    slope = set()
    count = 0
    for a in A:
        if a.y == 0:
            if a.x >= 0:
                m = float('inf')
            else:
                m = -float('inf')
        else:
            m = a.x / a.y

        item = (get_sign(a.x), get_sign(a.y), m)
        if item not in slope:
            slope.add(item)
            count += 1
    return slope


arr = [(3, 0), (-3, 0), (5, 0), (-5, 0), (0, 3),
       (0, 5), (0, -3), (0, -5), (2, 2), (3, 2)]
arr = [Point2D(z[0], z[1]) for z in arr]
solution(arr)
