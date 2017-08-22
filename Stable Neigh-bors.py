# from sortedcontainers import SortedList
import math
f = open('B-small-practice.in', 'r')
t = int(f.readline())

for tc in range(1, t + 1):
    maxt = -1
    print("Case #" + str(tc) + ": ", end = "")
    N, R, O, Y, G, B, V = map(int, f.readline().strip().split())
    col_num = {"R": R, "Y": Y, "B": B}
    num = [R, O, Y, G, B, V]

    if max(num) > N / 2:
        print("IMPOSSIBLE")
    else:
        result = []
        items = [[R, "R"],[Y, "Y"], [B, "B"]]
        i = 0
        while i< len(items):
            if items[i][0] == 0:
                del items[i]

        while len(result) < N:
            item1 = result[-1][1]
            if items[-1][0] == 1:
                del items[-1]
            if len()




        result = "".join(result)
        print(result)
