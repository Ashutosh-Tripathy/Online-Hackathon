num = [[20, 30, 40, 50, 60],
       [3, 4, 10, 17, 20],
       [5, 10, 15, 20, 30],
       [-100, 5, 10, 20, 100]]

result = num[0]
i = 1
while i < len(num):
    temp = num[i]
    if result[0] > temp[-1] or temp[0] > result[-1]:
        result = []
        break
    result = list(set(result).intersection(set(temp)))
    i = i + 1
print(result)