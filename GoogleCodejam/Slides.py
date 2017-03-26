
'''
Created on Dec 18, 2016

@author: tripathy
'''
# P R S

with open('B-small-practice.in') as f:
    content = f.readlines()
import copy

def get_slides(B, M):
    destination = B -1
    path_to_destination = set()
    result = []
    if (pow(2, B - 2) >= M):
        result = [[0 for x in range(B)] for y in range(B)]
        for a in range(B):
            for b in range(a + 1, B):
                if (M <= 0):
                    return result
                elif (a == 0 and b == destination):
                    continue
                result[a][b] = 1
                if (b != destination and result[b][destination] != 1):
                    result[b][destination] = 1
                    # M -= 1
                M -= 1
        if (M > 0):
            result[0][destination] = 1
    return result

number_of_test_cases = int(content.pop(0))
for y in range(number_of_test_cases):
    B, M = [int(x) for x in content.pop(0).split()]
    result = get_slides(B, M)
    if (len(result) == 0):
        print("Case #"+str(y+1)+": " + "IMPOSSIBLE")
    else:
        print("Case #"+str(y+1)+": " + "POSSIBLE")
        for item in result:
            print("".join([str(x) for x in item]))
    # print("\n\n\n\n\n\n\n\n\n\n")

# #
# # for x in range(5):
# #     print (x)
# R P S

# r-x p-x rp x
# r-x s-(r-x) rs (r-x)
# p-x = s -r + x
# r+p-s = 2x