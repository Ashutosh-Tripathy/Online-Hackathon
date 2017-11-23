from __future__ import division


def solution(A):
    num = int("".join(str(i) for i in reversed(A))) * 17
    result = 0
    while num > 0:
        result += num % 10
        num //= 10
    return result


print(solution([3, 5, 1]))
