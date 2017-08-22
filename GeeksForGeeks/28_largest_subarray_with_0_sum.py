items = [15, -2, 2, -8, 1, 7, 10, 23]
    # [15, 13, 15, 7, 8, 15, 25, 48]

index = {items[0]: 0}
result = 0
for i in range(1, len(items)):
    items[i] = items[i - 1] + items[i]
    if items[i] in index:
        result = max(result, i - index[items[i]])
    else:
        index[items[i]] = i
print(result)