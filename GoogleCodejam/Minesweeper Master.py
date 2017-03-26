with open('B-small-practice.in') as f:
    content = f.readlines()


def get_map():
    r, c = 0, 0
    global M
    global result
    while M > 0:
        if mini >= 3:
            inr, inc = 0, 0
            while M > 0:
                iniM = M
                for j in range(inc, mini):
                    if M == 0:
                        return
                    elif M == 1 and j == mini - 2:
                        break
                    result[inr][j] = "*"
                    inr += 1
                    M -= 1
                for i in range(inr, maxi):
                    if M == 0:
                        return
                    elif M == 1 and i == maxi - 2:
                        break
                    result[i][inc] = "*"
                    inc += 1
                    M -= 1
                if iniM == M:
                    possible = False
                    return
        if r >= maxi - 2 and c >= mini - 2:
            possible = False
            break

        elif M > mini:
            while c < mini:
                result[r][c] = "*"
                c += 1
            r += 1
            M -= mini
            c = 0
        elif M >= maxi - r:
            temp = r
            while temp < maxi:
                result[temp][c] = "*"
                temp += 1
            c += 1
            M -= maxi - r
        else:
            temp = r
            while M > 0:
                result[temp][c] = "*"
                temp += 1
                M -= 1
            c += 1
            if temp == R - 1:
                possible = False




T = int(content.pop(0))
for y in range(T):
    R, C, M = [int(x) for x in content.pop(0).split()]
    mini, maxi = min(R, C), max(R, C)
    result = [["." for x in range(mini)] for y in range(maxi)]
    possible = True



    print("Case #" + str(y+1) + ": ")

    if possible:
        print(result)
    else:
        print("Impossible")






















# while M > 0:
#         if mini > 3:
#             inr, inc = 0, 0
#             for i in range(inr, maxi):
#                 for j in range (inc, mini):
#                     if M == 0:
#                         return
#                     else:
#                         result[i][j] = "*"



