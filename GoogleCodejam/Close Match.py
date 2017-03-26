
'''
Created on Dec 18, 2016

@author: tripathy
'''
# P R S

with open('B-small-practice.in') as f:
    content = f.readlines()
import copy

def change_value(item, index, value):
    if (item[index] == "?"):
        item[index] = value

def fill_score(C, J, i):
    temp = []
    if (C[i] == "?" and J[i] == "?"):
        x = i + 1
        while (x < len(C)):
            if (C[x] == "?" and J[x] == "?"):
                C[x -1], J[x -1] = 0, 0
            else:
                break
            x += 1
        return C, J
    elif (C[i] == "?"):
        if (J[i] != "9"):
            # print(C[i])
            # print(J[i])
            C[i] = int(J [i]) + 1
            for x in range(i + 1, len(C)):
                change_value(J, x, 9)
                change_value(C, x,0)
            return C, J
        else:
            C[i] = int(J [i]) - 1
            for x in range(i + 1, len(C)):
                change_value(J, x, 0)
                change_value(C, x,9)
            return C, J
    elif (J[i] == "?"):
        if (C[i] != "9"):
            J[i] = int(C [i]) + 1
            for x in range(i + 1, len(C)):
                change_value(J, x, 0)
                change_value(C, x, 9)
            return C, J
        else:
            J[i] = int(C [i]) - 1
            for x in range(i + 1, len(C)):
                change_value(J, x, 9)
                change_value(C, x,0)
            return C, J
    elif (C[i] > J[i]):
        for x in range(i + 1, len(C)):
                change_value(J, x, 9)
                change_value(C, x,0)
        return C, J
    elif (J[i] > C[i]):
        for x in range(i + 1, len(C)):
            change_value(J, x, 0)
            change_value(C, x,9)
        return C, J
    else:
        return fill_score(C, J, i + 1)

def is_best_case_possible(C, J):
    for i in range(len(C)):
        if ((C[i] != J [i]) and C[i] != "?" and J[i] != "?"):
            return False
    return True
def get_best_case(C, J):
    for i in range(len(C)):
        if (C[i] == J [i]):
            change_value(J, i, 0)
            change_value(C, i ,0)
        elif (C[i] == "?"):
            C[i] = J [i]
        else:
            J[i] = C [i]
    return C, J

def get_close_match_score(C, J):
    if (is_best_case_possible(C, J)):
        result = get_best_case(C, J)
    else:
        result = fill_score(C, J, 0)
    return "".join(str(x) for x in result[0]), "".join(str(x) for x in result[1])

number_of_test_cases = int(content.pop(0))
for y in range(number_of_test_cases):
    C, J = [[y for y in x] for x in content.pop(0).split()]
    result = get_close_match_score(C, J)
    print("Case #"+str(y+1)+": " + " ".join(result))
