mat =  [[1,2,3,4,5],
        [3,4,5,6,7],
        [4,5,6,7,8],
        [5,6,7,8,9],]


def is_element_present(mat, item):
    X, Y = len(mat), len(mat[0])
    minx, miny = 0, 0
    while minx < X and miny < Y:
        i, j = minx + (X - minx)//2, miny + (Y-miny)//2
        # if min(i, j) < 0 or i >= len(mat) or j >= len(mat[0]):
        #     break

        if mat[i][j] == item:
            return True
        elif mat[i][j] > item:
            X, Y = i-1, j-1
        else:
            minx, miny = i + 1, j+1
    return False

print(is_element_present(mat, 8))