
def get_inversion_count(first, second):
    count = 0
    for item in second:
        i = len(first) -1
        while i > -1 and first[i] > item:
            i -= 1
        count += len(first) - 1 - i
    return count

def merger_sort(item, start, mid, end):
    temp = mid + 1
    while temp <= end:
        while start <= temp - 1:
            if item[start] >= item[temp]:
                tempv = item[temp]
                tempi = temp
                while tempi > start:
                    item[tempi] = item[tempi -1]
                    tempi -= 1
                item[start] = tempv
                temp += 1
            start += 1
        temp += 1



def inversion_count(item):
    group = 2
    start_index = 0
    result = 0

    while start_index + group -1 < len(item):
        start = start_index
        while start < len(item):
            end = start + group -1 if start + group -1 < len(item) else len(item) -1
            mid = start + (end - start) // 2
            first = item[start: mid+1]
            second = item[mid + 1: end +1]
            result += get_inversion_count(first, second)
            merger_sort(item, start, mid, end)
            start = end + 1
        group *= 2
    print(item)
    print(result)


print(inversion_count([1, 12, 13, 5, 6, 9, 10,3]))