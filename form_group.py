def solution(A):
    # write your code in Python 2.7
    group = []
    temp = A[0]
    for i in range(1, len(A)):
        if A[i] > A[i - 1]:
            group.append((A[i - 1], temp))
            temp = A[i]
    group.append((A[-1], temp))

    group.sort()
    print(group)
    for j in range(1, len(group)):
        item = group[j]
        prev = group[j - 1]
        if prev[1] > item[0]:
            return 1
    return len(group)


print(solution([1, 5, 4, 9, 8, 7, 14, 13, 15, 20, 25, 21]))
