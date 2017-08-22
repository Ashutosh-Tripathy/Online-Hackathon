def find_duplicate(arr):
    i = 0
    while i < len(arr):
        if(arr[abs(arr[i])] >= 0):
            arr[abs(arr[i])] = - arr[abs(arr[i])]
        else:
            print(abs(arr[i]))
        i += 1


find_duplicate([2, 3, 4, 7, 100, 3, 4, 50])
