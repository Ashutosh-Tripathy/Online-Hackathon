mat = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]

counter, L = 0, len(mat)

while counter < L // 2:
    i, j = counter, counter
    while j < L - 1 - counter:
        temp = mat[i][j]
        mat[i][j] = mat[L - 1 -j][i]
        mat[L - 1 -j][i] = mat[L - 1 -i][L - 1 -j]
        mat[L - 1 -i][L - 1 -j] = mat[j][L - 1 -i]
        mat[j][L - 1 -i] = temp
        print("\n".join(["".join(str(x)) for x in mat]))
        print("--------------------------")
        j += 1
    counter += 1
