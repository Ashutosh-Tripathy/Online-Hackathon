
'''
Created on Dec 18, 2016

@author: tripathy
'''
# P R S
import math
with open('B-small-practice.in') as f:
    content = f.readlines()

def get_tie_probability(tie_probability, K):
    # print(K)
    mid, result = K / 2, 0
    top = tie_probability.pop()
    calculate_probability =[[top, 1], [1 - top, 0]]
    for item in tie_probability:
        temp = []
        for prob in calculate_probability:
            if (prob[1] <= mid):
                temp.append([prob[0] * item, prob[1] + 1])
            temp.append([prob[0] * (1 - item), prob[1]])
        calculate_probability = temp
        # print(calculate_probability)
    for item in calculate_probability:
        if (item[1] == mid):
            result += item[0]
    # print(mid)
    return(round(result, 10))

def get_max_tie_probability(N, K, probability):
    probability.sort()
    # tie_probability = []
    # while (K > 0):
    #     tie_probability.append(probability.pop())
    #     tie_probability.append(probability.pop(0))
    #     # top, bottom = probability.pop(), probability.pop(0)
    #     # tie_probability *= ((top * (1 - bottom)) + (bottom * (1 - top)))
    #     K -= 2
    return str(get_tie_probability(probability, K))

player_winner_map = {"P" : "PR", "R" : "RS", "S": "PS"}
number_of_test_cases = int(content.pop(0))
for y in range(number_of_test_cases):
    N, K = [int(x) for x in content.pop(0).split()]
    probability = [float(x) for x in content.pop(0).split()]
    print("Case #"+str(y+1)+": " + get_max_tie_probability(N, K, probability))
