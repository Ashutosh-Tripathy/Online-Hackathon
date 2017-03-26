
'''
Created on Dec 18, 2016

@author: tripathy
'''

import copy
import math

with open('B-small-practice.in') as f:
    content = f.readlines()


def get_total_number(prerequisiteNameMap, N):
    total_number = 1
    for item in prerequisiteNameMap:
        if (item != 0):
            total_number *= math.factorial(len(prerequisiteNameMap[item]))/math.factorial(len(prerequisiteNameMap[item]) + 1)
    return total_number * math.factorial(N)

def fraction_of_possible_course_sequence(N, prerequisite, course_name, number_of_cool_words, cool_words):
    prerequisiteNameMap = {}
    for x in  range(N):
        if (prerequisite[x] in prerequisiteNameMap):
            prerequisiteNameMap[prerequisite[x]].append(course_name[x])
        else:
            prerequisiteNameMap[prerequisite[x]] = [course_name[x]]
    total_number = get_total_number(prerequisiteNameMap, N)
    print(total_number)
    valid_number = []
    for cool_word in cool_words:
        valid_numbers = []
        temp = copy.deepcopy(prerequisiteNameMap)
        present = True
        counter = 0
        for y in cool_word:
            while (counter not in temp or y not in temp[counter]):
                counter += 1
                if (counter > N):
                    present = False
                    break
            if (present):
                temp[counter].remove(y)
        if (present):
            valid_number.append(getPossibleNumber(prerequisiteNameMap, cool_word))
        else:
            valid_number.append(0.0)
    return valid_number


number_of_test_cases = int(content.pop(0))
for x in range(number_of_test_cases):
    N = int(content.pop(0))
    prerequisite = [int(x) for x in content.pop(0).split()]
    course_name = [x for x in list(content.pop(0))]
    number_of_cool_words = int(content.pop(0))
    cool_words = [x for x in content.pop(0).split()]

    print("Case #"+str(x+1)+": " + ' '.join(str(x) for x in fraction_of_possible_course_sequence(N, prerequisite, course_name, number_of_cool_words, cool_words)))

#
# for x in range(5):
#     print (x)
