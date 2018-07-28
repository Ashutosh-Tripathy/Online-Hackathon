mat = [ [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16],
        [17,18,19,20]
    ]

def should_change_direction(i, j, visited_index):
    return (i, j) in visited_index or min(i,j) < 0 or i == len(mat) or j == len(mat[0])

def get_next_cordinate(i, j, current_direction):
    nexti, nextj = i, j
    if current_direction == 0:
       nextj += 1
    elif current_direction == 1:
        nexti += 1
    elif current_direction == 2:
        nextj -= 1
    else:
        nexti -= 1
    return (nexti, nextj)

def print_mat(mat):
    visited_index = set() 
    j, k, direction = 0, 0, 0
    for i in range(len(mat) * len(mat[0])):
        print(mat[j][k])
        visited_index.add((j,k))
        newj, newk = get_next_cordinate(j, k, direction)
        if should_change_direction(newj, newk, visited_index):
            direction = (direction + 1)%4
            newj, newk = get_next_cordinate(j, k, direction)

        j, k = newj, newk
print_mat(mat)
