from __future__ import division


def solution(A):
    # write your code in Python 2.7
    sum = 0
    carry = 0
    for i in range(len(A)):
        num = 17 * A[i] + carry
        sum = sum + (num % 10)
        carry = num // 10
        i += 1
    sum += carry
    return sum


solution([3, 5, 1])
