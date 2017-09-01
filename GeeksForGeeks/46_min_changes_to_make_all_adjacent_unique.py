arr = [1,1, 4, 2, 3, 4, 4]
non_uniques_indexs = []
i = 1

while i < len(arr):
    index = []
    if arr[i] == arr[i-1]:
        index.append(i-1)
        while i < len(arr) and arr[i] == arr[i-1]:
            index.append(i)
            i += 1
        non_uniques_indexs.append(index)
    else:
        i += 1

print(non_uniques_indexs)