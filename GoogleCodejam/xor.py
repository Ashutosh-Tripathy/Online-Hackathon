f = open('B-small-practice.in', 'r')
# 2  5 7 1 4 9 12 10 0
numbers = [int(x) for x in f.readline().split()]
k = 70000
start, end = 0, len(numbers) - 1
while True:
    key = numbers[end]
    low, high = start, end - 1
    print(low, high)
    while low <= high:
        if numbers[low] < key:
            low += 1
            continue
        else:
            if numbers[high] > key:
                high -= 1
                continue
            else:
                numbers[low], numbers[high] = numbers[high], numbers[low]
                low += 1
                high -= 1
    numbers[high + 1], numbers[end] = numbers[end], numbers[high + 1]
    if high + 1 == k:
        break
    elif high + 1 > k:
        end = high
    else:
        start = low
print(numbers[high + 1])
