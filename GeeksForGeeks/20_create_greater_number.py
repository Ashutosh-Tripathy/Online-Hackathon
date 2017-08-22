num = 10104

num = list(str(num))
i = len(num) - 1

while i > 0:
    if num[i] > num[i -1]:
        num[i], num[i - 1] = num[i - 1], num[i]
        break
    else:
        i -= 1

print(int("".join(num)))

