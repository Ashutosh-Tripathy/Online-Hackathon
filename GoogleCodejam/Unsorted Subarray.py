array = [10, 12, 20, 30, 101, 0, 25, 40, 32, 31, 35, 50, 60]
start = end = -1
min_num, max_num = 100000, -1

for i in range(1, len(array)):
    if array[i] < array[i - 1]:
        if array[i] < min_num:
            min_num = array[i]
            if start == -1:
                start = i - 2
            while start > -1:
                if min_num < array[start]:
                    start -= 1
                else:
                    break
            start += 1
        if array[i - 1] > max_num:
            max_num = array[i - 1]
            end = i + 1
            while end < len(array):
                if max_num > array[end]:
                    end += 1
                else:
                    break
            end -=1
print(start,end)