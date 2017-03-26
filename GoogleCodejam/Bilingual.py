from decimal import *
from pulp import *
with open('B-small-practice.in') as f:
    content = f.readlines()
getcontext().prec = 18

T = int(content.pop(0))
for y in range(T):
    N = int(content.pop(0).strip())
    commonword = set()
    eng = set(content.pop(0).strip().split())
    french =set(content.pop(0).strip().split())
    unknown = [content.pop(0).strip().split() for i in range(N - 2)]
    result = 0

    for item in unknown:
        ecount, fcount = 0, 0
        eword, fword = [], []
        for item1 in item:
            if item1 not in eng:
                # ecount += 1
                eword.append(item1)
            if item1 not in french:
                # fcount += 1
                fword.append(item1)
        # result += min(ecount, fcount)
        if len(eword) <= len(fword):
            eng = eng.union(eword)
        else:
            french = french.union(fword)

    for e in eng:
        if e in french:
            if e not in commonword:
                commonword.add(e)
                # result += 1

        # commonword = commonword.union(eword) if len(eword) < len(fword) else commonword.union(fword)
    print("Case #" + str(y+1) + ": " + str(len(commonword)))
