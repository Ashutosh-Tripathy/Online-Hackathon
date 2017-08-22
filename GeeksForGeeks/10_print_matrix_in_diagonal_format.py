print_diagonal(i, j, is_up):
    if is_up:
        while i > -1 and j <= J :
            i -= 1
            j += 1
            print(i, j)
    else:
        while i <= I and j > -1:
            i += 1
            j -= 1
            print(i, j)

def print_diagonal_form(matrix):
    I, J = len(matrix) -1, len(matrix[0]) -1
    i, j = 0, 0
    is_up = True
    print_diagonal(i, j, is_up)

    is_up = not is_up if is_up else is_up

print_diagonal_form([[1,2,3],[4,5,6]])