def solution(A):
    # write your code in Python 2.7
    group = []
    temp = A[0]
    for i in range(1, len(A)):
        if A[i] > A[i - 1]:
            group.append((A[i - 1], temp))
            temp = A[i]
    
    group.sort()
    for j in range(1, len(group)):
        item = group[j]
        prev_item = group[j - 1]
        if item[0] < prev_item[0] and prev_item[1] < item[1]:
            return 1

    return len(group)


solution([1, 5, 4, 9, 8, 7, 12, 13, 14])
