import math
def get_min_cost(matrix, i, j):
    if i == 0 and j == 0:
        return matrix[i][j]
    elif i < 0 or j < 0:
        return float('inf')
    min_count = min(matrix[i][j] + get_min_cost(matrix, i, j -1), matrix[i][j] + get_min_cost(matrix, i - 1, j))
    return min_count

print(get_min_cost([[1, 7, 9, 2], [8, 6, 3, 2], [1, 6, 7, 8], [2, 9, 8, 2]], 3, 3))