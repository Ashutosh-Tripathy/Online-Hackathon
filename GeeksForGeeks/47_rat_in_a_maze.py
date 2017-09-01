mat = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]]

# i, j = len(mat)-1, len(mat[0])-1

# result = [[float('inf') for y in range(j + 1) ] for x in range(i + 1)]
# result[i][j] = 0
# destination = mat[i][j]
# queue = [(i, j)]
# while len(queue) > 0:
#     i, j = queue.pop(0)
#     if min(i, j) >= 0:
#         if i > 0 and mat[i-1][j] == 1:
#             result[i-1][j] = min(result[i][j] + 1, result[i-1][j + 1] + 1)
#             queue.append((i-1, j))
#         if j > 0 and mat[i][j -1] == 1:
#             result[i][j-1] = min(result[i][j] + 1, result[i-1][j - 1] + 1)
#             queue.append((i, j-1))            
# print(result[0][0])

reached_destination = False
final_result = []
def mark_and_move(mat, result, x, y):
    global reached_destination, final_result
    if reached_destination or x >= len(mat) or y >= len(mat[0]) or mat[x][y] != 1:
        return
    result[x][y] = 1
    if x == len(mat) -1 and y == len(mat[0]) -1:
        reached_destination = True
        final_result = result
    mark_and_move(mat, result, x +1, y)
    mark_and_move(mat, result, x, y + 1)
    if not reached_destination:
        result[x][y] = 0

    # global reached_destination, final_result
    # if x == len(mat)-1 and y == len(mat[0])-1:
    #     result[x][y] = 1
    #     final_result = result
    #     reached_destination = True
    # if reached_destination or (x >= len(mat) and y >= len(mat[0])):
    #     return    
    # result[x][y] = 1
    # if x+1 < len(mat) and mat[x + 1][y] == 1:
    #     mark_and_move(mat,result,x+1, y)
    # if y+1 < len(mat[0]) and mat[x][y+1] == 1:
    #     mark_and_move(mat,result,x, y+1)
    
    # if not reached_destination:
    #     result[x][y] = 0


def back_track(mat):
    i, j = len(mat)-1, len(mat[0])-1
    result = [[0 for y in range(j + 1)] for x in range(i + 1)]
    mark_and_move(mat, result, 0, 0)

back_track(mat)
print(final_result)







    