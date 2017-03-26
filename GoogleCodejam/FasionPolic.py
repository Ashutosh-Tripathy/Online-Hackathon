
'''
Created on Dec 18, 2016

@author: tripathy
'''
# P R S

with open('B-small-practice.in') as f:
    content = f.readlines()
import copy

def is_next_item_available(item):
    if ((item[0] < J and combination_map["21"] < K) or (item[1] < P and combination_map["31"] < K) or (item[2] < S and combination_map["32"] < K)):
        return True
    else:
        j, k, s = item[0] < J, item[1] < P, item[2] < S
        if ((j and k) or (k and s) or (s and j)):
            return True
        else:
            return False

def get_new_item(item):
    result = copy.deepcopy(item)
    if (item[2] < S and combination_map["32"] < K):
        combination_map["32"] += 1
        result[2] += 1
    elif (item[1] < P and combination_map["31"] < K):
        combination_map["21"] = 1
        combination_map["32"] = 1
        combination_map["31"] = 1
        result[2] = 1
        result[1] += 1
    elif (item[1] < J and combination_map["21"] < K):
        combination_map["31"] = 1
        combination_map["32"] = 1
        combination_map["21"] = 1
        result[2] = 1
        result[1] = 1
        result[0] += 1
    else:
        j, k, s = item[0] < J, item[1] < P, item[2] < S
        if (k and s):
            result[2] += 1
            result[1] += 1
            combination_map["21"] = 1
            combination_map["32"] = 1
            combination_map["31"] = 1
        elif (j and k):
            result[1] += 1
            result[0] += 1
            combination_map["21"] = 1
            combination_map["32"] = 1
            combination_map["31"] = 1
        else:
            result[0] += 1
            result[2] += 1
            combination_map["21"] = 1
            combination_map["32"] = 1
            combination_map["31"] = 1
    return result


def get_outfit(J, P, S, K):
    result = [[1, 1, 1]]
    while (is_next_item_available(result[len(result) - 1])):
        result.append(get_new_item(result[len(result) - 1]))
    return result

number_of_test_cases = int(content.pop(0))
for y in range(number_of_test_cases):
    combination_map = {"32" : 1, "31": 1, "21" : 1}
    J, P, S, K = [int(x) for x in content.pop(0).split()]
    result = get_outfit(J, P, S, K)
    print("Case #"+str(y+1)+": " + str(len(result)))
    for item in result:
        print(item[0], item[1], item[2])

# #
# # for x in range(5):
# #     print (x)
# R P S

# r-x p-x rp x
# r-x s-(r-x) rs (r-x)
# p-x = s -r + x
# r+p-s = 2x