mat = [['a', 'c', 'x'], ['h', 'b', 'e'], ['i', 'g', 'f']]
#mat = [['a', 'b'], ['d', 'c']]

longest_path = {}


def convert_mat(mat):
    return [[ord(x) for x in y] for y in mat]


def get_cordinate_value(mat, M, N, i, j):
    return -1 if min(i, j) < 0 or i >= M or j >= N else mat[i][j]


def get_longest_path_for_coordinate(mat, M, N, i, j, current_length, track_length):
    if min(i, j) < 0 or i >= M or j >= N:
        return current_length
    
    if (i, j) in track_length:
        return track_length[(i, j)] 

    result = [0]
    cordinates = {(i - 1, j), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j),
                  (i + 1, j - 1), (i + 1, j + 1), (i, j - 1), (i, j + 1)}
    for c in cordinates:
        k, l = c
        if get_cordinate_value(mat, M, N, k, l) - mat[i][j] == 1:
            result.append(get_longest_path_for_coordinate(mat, M, N, k, l,  1, track_length))
    max_length = max(result)  
    track_length[(i,j)] = current_length + max_length
    return track_length[(i,j)] 


def get_lognest_path(mat):
    mat = convert_mat(mat)
    M, N = len(mat), len(mat[0])
    track_length = {}
    for i in range(M):
        for j in range(N):
            get_longest_path_for_coordinate(mat, M, N, i, j, 1, track_length)
    print(max(track_length.values()))


get_lognest_path(mat)
# def get_longest_path(mat, M, N, i, j, longest_path, length):
#     if min(i, j) < 0 or i>=M or l >=N:
#         return 0

#     cordinates = {(i-1, j), (i-1, j-1), (i-1, j +1), (i+1, j), (i+1, j-1), (i+1, j+1), (i, j-1), (i, j+1)}
#     result = []
#     for c in cordinates:
#         k, l = c

# def find_longest_path(mat):
#     mat = convert_mat(mat)
#     M, N = len(mat), len(mat[0])

#     for i in range(M):
#         for j in range(N):
#             if (i, j) not in longest_path:
#                 longest_path[(i, j)] = get_longest_path(mat, M, N, i, j, longest_path, 1)
