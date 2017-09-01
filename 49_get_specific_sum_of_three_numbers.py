arr = [0, -1, 1, 2, -2, 3, -3, 4, -4]


def get_combination_of_numbers(arr):
    arr.sort()
    k = 2
    result = []
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            k = j + 1
            sum_of_two_element = arr[i] + arr[j]
            if sum_of_two_element > 0:
                break
            while k < len(arr) and sum_of_two_element + arr[k] < 0:
                k += 1
            temp = k
            while temp < len(arr) and sum_of_two_element + arr[temp] == 0:
                result.append((arr[i], arr[j], arr[temp]))
                temp += 1

    return result


print(get_combination_of_numbers(arr))
