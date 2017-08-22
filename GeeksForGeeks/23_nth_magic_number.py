n = 5


def get_nth_magic_number(n):
    pow, answer = 1, 0
    while n:
        pow = pow * 5
        if n & 1:
            answer += pow
        n >>= 1
    return answer

print(get_nth_magic_number(n))
