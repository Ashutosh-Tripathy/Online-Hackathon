items = [10, 20, 30, 50, 10, 70, 30]
result = [0 for x in range(len(items))]

for i in range(len(items)):
    for j in range(0, len(items) -i):
        if j == 0:
            temp = items[i]
        else:
            temp = min(items[i], result[max(i-1, 0)])
        result[j] = max(result[j], temp)

print(result)