'''
Created on Dec 18, 2016

@author: tripathy
'''

with open('A-large-practice.in') as f:
    content = f.readlines()

def maximum_point_for_case(S):
    maximum_point = 0
    request = []
    while len(S) > 0:
        element = S.pop(0)
        if (len(request) == 0):
            request.append(element)
        elif (request[-1] == element):
            request.pop()
            maximum_point += 10
        elif (len(request) < len(S)):
            request.append(element)
        else:
            request.pop()
            maximum_point += 5

    return maximum_point

number_of_test_cases = int(content.pop(0))
for x in range(number_of_test_cases):
    S = list(content.pop(0))
    print("Case #"+str(x+1)+": "+str(maximum_point_for_case(S)))

#
# for x in range(5):
#     print (x)