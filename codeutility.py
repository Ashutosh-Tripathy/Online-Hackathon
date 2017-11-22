# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 2.7
    A.sort()
    i = 0
    num = 1
    while i < len(A) and A[i] <= 0:
        i += 1

    while i < len(A):
        if A[i] == num:
            num+=1
        elif A[i] > num:            
            break        
        i += 1
    return num