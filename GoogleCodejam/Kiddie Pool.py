from decimal import *

with open('B-small-practice.in') as f:
    content = f.readlines()
getcontext().prec = 18

T = int(content.pop(0))
for y in range(T):
    N, V, C = map(Decimal, content.pop(0).split())
    # CR = []
    # for n in range(int(N)):
    #     temp = [Decimal(x) for x in reversed(content.pop(0).strip().split())]
    #     CR.append(temp)
    CR = [[Decimal(x) for x in reversed(content.pop(0).strip().split())] for n in range(int(N))]
    CR.sort()
    sumvt = sum(cr[0] * cr[1] for cr in CR)
    sumv = sum(cr[1] for cr in  CR)
    avgT = sumvt / sumv
    impossible = False
    hotter, cooler = False, False
    prev = 0
    while round(avgT, 6) != round(C, 6):
        if len(CR) == 0:
            impossible = True
            break
        if avgT > C:
            item = CR.pop()
            hotter = True
        else:
            item = CR.pop(0)
            cooler = True
        if hotter and cooler:
            x =(sumvt - (C * sumv)) / (C - prev[0])
            # sumvt += item[0] * x
            sumv += x
            break
            # sumvt/ sumv = C
        else:
            sumvt -= item[0] * item[1]
            sumv -= item[1]
        if sumv == 0:
            impossible = True
            break
        avgT = sumvt / sumv
        prev = item
    if impossible:
        print("Case #" + str(y+1) + ": " + "IMPOSSIBLE")
    else:
        print("Case #" + str(y+1) + ": " + str(V / sumv))
