def get_count():
    order = [[2, 1, 0, 2, 1], [0, 0, 1, 2, 1], [1, 0, 0, 2, 1]]

    ones, twos = [], set()
    for i in range(len(order)):
        for j in range(len(order[i])):
            if order[i][j] == 1:
                ones.append((i, j))
            elif order[i][j] == 2:
                twos.add((i, j))

    counter = 0
    rot_count = []
    while len(ones) > 0:
        k = 0
        while k < len(ones):
            # print(k)
            i, j = ones[k]
            if len(set([(i, j+1), (i, j-1), (i+1, j), (i-1,j)]).intersection(twos)) > 0:
                rot_count.append((i,j))
                ones.pop(k)
            else:
                k += 1
        if len(rot_count) == 0:
            return -1
        else:
            counter += 1
            for item in rot_count:
                twos.add(item)
            rot_count = []
    return counter

result = get_count()
if result == -1:
    print('Not possible ')
else:
    print(result)
