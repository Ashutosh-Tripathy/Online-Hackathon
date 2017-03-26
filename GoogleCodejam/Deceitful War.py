from decimal import *
with open('B-small-practice.in') as f:
    content = f.readlines()

T = int(content.pop(0))
for a in range(T):
    I = int(content.pop(0).strip())
    N = sorted([Decimal(x) for x in content.pop(0).split()])
    K = sorted([Decimal(x) for x in content.pop(0).split()])

    warcount, dwarcount = 0, 0
    ni, ki = I - 1, I - 1
    while ni > -1:
        if N[ni] > K[ki]:
            warcount += 1
        else:
            ki -= 1
        ni -= 1
    ni, ki = I - 1, I - 1
    while ki > -1:
        if N[ni] > K[ki]:
            dwarcount += 1
            ni -= 1
        ki -= 1
    print("Case #" + str(a+1) + ": " + str(dwarcount) + " " + str(warcount))

    # MN = N
    # N = I
    # MK = K
    # y = 0
    # i = 0
    # for j in range(N):
    #     while i < N and MN[i] < MK[j]:
    #         i += 1
    #     if i < N:
    #         y += 1
    #         i += 1
    # z = N
    # j = 0
    # for i in range(N):
    #     while j < N and MN[i] > MK[j]:
    #         j += 1
    #     if j < N:
    #         z -= 1
    #         j += 1
    # print("Case #" + str(a+1) + ": " + str(y) + " " + str(z))

