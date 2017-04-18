# from sortedcontainers import SortedList
import math
f = open('B-small-practice.in', 'r')
t = int(f.readline())


for tc in range(1, t + 1):
    print("Case #" + str(tc) + ": ", end = "")
    N, P = map(int, f.readline().split())
    result = 0
    R = [int(x) for x in f.readline().strip().split()]
    Q = []
    [Q.append(sorted([int(x) for x in f.readline().strip().split()])) for n in range (N)]
    while True:
        endloop = False
        for i in range(N):
            if len(Q[i]) == 0:
                endloop = True
        if endloop: break
        k = [Q[i][0]/R[i] for i in range(N)]
        mink, maxk = 10000000000, -1
        for i in range(N):
            temp = Q[i][0]/R[i]
            if temp < mink:
                mink = temp
                mini = i
            if temp > maxk:
                maxk = temp
                maxi = i
        mink, maxk = min(k), max(k)
        count = math.ceil(mink)
        while True:
            if Q[mini][0]/R[mini] * count >= .9:
                if Q[maxi][0]/ R[maxi] * count <= 1.1:
                    [Q[i].pop(0) for i in range(N)]
                    result += 1
                    break
                else:
                    count += 1
            else:
                [Q[i].pop(0) for i in range(N) if Q[i][0]/R[i] == mink]

    print(result)

